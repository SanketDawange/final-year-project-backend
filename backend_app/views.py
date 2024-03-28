from django.shortcuts import render
import joblib
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
import json
from django.http import JsonResponse
import random
from .models import SensorData
from django.utils.dateparse import parse_datetime
import requests
from .send_sms import send
from django.utils import timezone
from datetime import timedelta
from django.core.exceptions import ObjectDoesNotExist
from .models import Alert

# views.py

from django.shortcuts import render

def index(request):
    return render(request, 'index.html')


def create_alert(temp):
    Alert.objects.create(alert_message=f"Your vehicle temperature crossed 40 degrees Celsius. Current temperature: {temp}")


def send_alert(temp, temp_limit):
    # Fetch the most recent Alert object
    msg = "Your vehicle temperature crossed "+ str(temp_limit)+" degrees Celsius. Current temperature "

    try:
        recent_alert = Alert.objects.latest('created_at')
        # Check if the most recent alert is older than 5 minutes
        if timezone.now() - recent_alert.created_at > timedelta(minutes=5):
            send(msg+ str(temp))
            create_alert(temp)
    except ObjectDoesNotExist:
        # If no Alert objects exist, send the alert
        send(msg+ str(temp))
        create_alert(temp)

@csrf_exempt 
def getData(request):
    try:
        get_sensor_data()

        # FETCH LATEST VALUES FROM DB
        latest_record = SensorData.objects.latest('created_at')

        gas_concentration = latest_record.field1
        temp = latest_record.field2
        # temp = 41
        humidity = latest_record.field3
        temp_limit = 25
        if temp >= temp_limit:

            print("################## Sending alert")
            send_alert(temp,temp_limit)

        else:
            print("################## Not sending alert")

        dht11_model_path = 'backend_app\ml\dht11\comfort_level_model.joblib'
        mqt135_model_path = 'backend_app\ml\mqt135\gas_concentration.joblib'

        dht11_model = joblib.load(dht11_model_path)
        mqt135_model = joblib.load(mqt135_model_path)

        comfort_level_input = [[temp, humidity]]
        concentration_input = float(gas_concentration)
        concentration_input = [[concentration_input]]

        predicted_value = dht11_model.predict(comfort_level_input)
        predicted_gas = mqt135_model.predict(concentration_input)[0]

        if predicted_value == 0:
            predicted_comfort= "High"
        elif predicted_value == 1:
            predicted_comfort= "Low"
        elif predicted_value == 2:
            predicted_comfort= "Moderate"

        response = {
            "status": "success",
            "predicted_comfort_level" : predicted_comfort,
            "predicted_gas": predicted_gas,
            "temp": temp,
            "humidity":humidity,
            "gas_concentration":gas_concentration
        }

        return JsonResponse(response)

    except Exception as e:
        error_response = {
            "status": "error",
            "message": str(e)
        }
        return JsonResponse(error_response)

@csrf_exempt
@require_POST
def webhook_receiver(request):
    return JsonResponse({'status': 'success'})

def get_sensor_data():

    url = "https://api.thingspeak.com/channels/2372014/feeds.json?api_key=55IVI0B5NDYV5DFZ"

    response = requests.get(url)
    data = response.json()

    for entry in data['feeds']:
        created_at = parse_datetime(entry['created_at'])
        entry_id = entry['entry_id']
        field1 = entry['field1']
        field2 = entry['field2']
        field3 = entry['field3']
        field4 = entry['field4']

        # Check if a record with the same timestamp already exists
        existing_record = SensorData.objects.filter(created_at=created_at).first()

        if existing_record:
            # Update the existing record or handle as needed
            existing_record.field1 = field1
            existing_record.field2 = field2
            existing_record.field3 = field3
            existing_record.field4 = field4
            existing_record.save()
        else:
            # Create a new record if it doesn't exist
            sensor_data = SensorData.objects.create(
                created_at=created_at,
                entry_id=entry_id,
                field1=field1,
                field2=field2,
                field3=field3,
                field4=field4
            )
            sensor_data.save()

    return JsonResponse({'status': 'success'})
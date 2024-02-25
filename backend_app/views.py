from django.shortcuts import render
import joblib
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import random
# views.py

from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

@csrf_exempt 
def getData(request):
    try:

        # FETCH LATEST VALUES FROM DB


        temp = random.uniform(0, 40)
        humidity = random.uniform(0, 140)
        gas_concentration = random.uniform(5, 1000)


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
            "humidity":humidity
        }

        return JsonResponse(response)

    except Exception as e:
        error_response = {
            "status": "error",
            "message": str(e)
        }
        return JsonResponse(error_response)

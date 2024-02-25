from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('get_data/', views.getData, name='get_data')
]

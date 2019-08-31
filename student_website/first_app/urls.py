"""
Section : URL MAPPING

This file is created by Samyak Gaur
We create this file so that we can use the include function in 
in the projects url file and tell it to import all the urls 
mentioned here 
"""

from django.urls import path
from first_app import views

urlpatterns = [
    path('first_app_url',views.index),
    # adding the template url here 
    path('help',views.help),
    path('index1',views.index1),
    path('index12',views.report),
]

"""
This will basically work as 
127.0.0.8000/first_app/first_app_url

As first_app is mentioned in the urls.py file of the project

"""
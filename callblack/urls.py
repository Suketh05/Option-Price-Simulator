from django.urls import path
from . import views
urlpatterns = [
    path('', views.callblack),
    path('Call_Black_scholes_model/', views.calc_call_Black_Scholes)
]

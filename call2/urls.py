from django.urls import path
from . import views
urlpatterns = [
    path('', views.call2),
    path('Call_2_step_binomial/', views.calc_call_TwoStep_Binomial),
]

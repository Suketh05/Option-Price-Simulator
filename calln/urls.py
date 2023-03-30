from django.urls import path
from . import views
urlpatterns = [
    path('', views.calln),
    path('Call_n_step_binomial/', views.calc_call_nStep_binomial),
]

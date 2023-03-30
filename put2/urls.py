from django.urls import path
from . import views
urlpatterns = [
    path('', views.put2),
    path('Call_2_step_binomial/', views.calc_put_TwoStep_Binomial),
]

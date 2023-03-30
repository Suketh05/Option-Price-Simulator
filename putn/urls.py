from django.urls import path
from . import views
urlpatterns = [
    path('', views.putn),
    path('Call_n_step_binomial/', views.calc_put_nStep_binomial),
]

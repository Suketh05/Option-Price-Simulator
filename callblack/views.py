from django.shortcuts import render
import numpy as np
from scipy.stats import norm

# Create your views here.
def callblack(request):
    return render(request,'callblack.html')

def calc_call_Black_Scholes(request):
    sigma = float(request.GET['volatility'])
    r = float(request.GET['rate'])
    s0 = float(request.GET['InitialStockPrice'])
    k0 = float(request.GET['StrikePrice'])
    t0 = float(request.GET['Maturity'])

    t0=t0/365

    d1 = (np.log(s0 / k0) + (r + sigma ** 2 / 2) * t0) / (sigma * np.sqrt(t0))
    d2 = d1 - sigma * np.sqrt(t0)

    price = s0 * norm.cdf(d1, 0, 1) - k0 * np.exp(-r * t0) * norm.cdf(d2, 0, 1)

    return render(request, 'output.html', {'result': price})
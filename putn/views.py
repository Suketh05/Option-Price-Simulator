from django.shortcuts import render
import math

# Create your views here.
def putn(request):
    return render(request,'putn.html')

def calc_put_nStep_binomial(request):
    n = int(request.GET['steps'])
    r = float(request.GET['rate'])
    u = float(request.GET['increment'])
    d = float(request.GET['decrement'])
    s0 = float(request.GET['InitialStockPrice'])
    k0 = float(request.GET['StrikePrice'])
    t0 = float(request.GET['Maturity'])
    e = 2.718281828459045
    tu = t0 / n
    p = (pow(e, r * tu) - d) / (u - d)
    c0 = float(0)
    for j in range(0,n+1):
        a = math.factorial(n)
        b = math.factorial(n-j)*math.factorial(j)
        c = a/b
        c0 = c0+c*pow(p,j)*pow(1-p,n-j)*max(k0-s0*pow(u,j)*pow(d,n-j),0)

    c0 = c0*pow(e,-r*t0)

    return render(request, 'output.html', {'result': c0})

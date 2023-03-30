from django.shortcuts import render

# Create your views here.

def put2(request):
    return render(request,'put2.html')

def calc_put_TwoStep_Binomial(request):
    r = float(request.GET['rate'])
    u = float(request.GET['increment'])
    d = float(request.GET['decrement'])
    s0 = float(request.GET['InitialStockPrice'])
    k0 = float(request.GET['StrikePrice'])
    t0 = float(request.GET['Maturity'])
    e = 2.718281828459045
    tu = t0/2
    p = (pow(e,r*tu)-d)/(u-d)
    c0 = (max(k0-s0*pow(u,2),0)*pow(p,2)+max(k0-s0*pow(d,2),0)*pow(1-p,2)+2*max(k0-s0*u*d,0)*p*(1-p))*pow(e,-r*t0)
    return render(request,'output.html',{'result':c0})

from django.shortcuts import render

# Create your views here.

def distance(request):
    result=None
    if request.method=='POST':
        value=float(request.POST.get('value'))
        conversion=request.POST.get('conversion')
        if conversion == 'm_to_km':
            result = f"{value} meters = {value / 1000:.4f} kilometers"
        elif conversion == 'km_to_m':
            result = f"{value} kilometers = {value * 1000:.2f} meters"
        elif conversion == 'm_to_mile':
            result = f"{value} meters = {value / 1609.34:.4f} miles"
        elif conversion == 'mile_to_m':
            result = f"{value} miles = {value * 1609.34:.2f} meters"
        elif conversion == 'km_to_mile':
            result = f"{value} kilometers = {value / 1.60934:.4f} miles"
        elif conversion == 'mile_to_km':
            result = f"{value} miles = {value * 1.60934:.2f} kilometers"

    return render(request, 'Distance.html', {'result': result})

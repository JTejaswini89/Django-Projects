from django.shortcuts import render

# Create your views here.
def unitconverter(request):
    result=None
    if request.method=="POST":
        value=float(request.POST.get('value'))
        conversion=request.POST.get('conversion')

        if conversion == 'c_to_f':
            result = f"{value} °C = {(value * 9/5) + 32:.2f} °F"
        elif conversion == 'f_to_c':
            result = f"{value} °F = {(value - 32) * 5/9:.2f} °C"
        elif conversion == 'c_to_k':
            result = f"{value} °C = {value + 273.15:.2f} K"
        elif conversion == 'k_to_c':
            result = f"{value} K = {value - 273.15:.2f} °C"
        elif conversion == 'f_to_k':
            result = f"{value} °F = {((value - 32) * 5/9) + 273.15:.2f} K"
        elif conversion == 'k_to_f':
            result = f"{value} K = {((value - 273.15) * 9/5) + 32:.2f} °F"

    return render(request, 'unitconverter.html', {'result': result})
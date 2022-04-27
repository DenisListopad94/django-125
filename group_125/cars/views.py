from django.shortcuts import render, redirect
from django.http import HttpResponse,HttpResponseNotFound
from cars.models import Car
# Create your views here.
lst_car=['bmw','volvo','tesla']

# cars_models=[
#     {'url_name':'bmw'},
#     {'url_name':'volvo'},
#     {'url_name':'tesla'},
# ]
# dict_cars={
#     'cars': lst_car,
#     'urls':cars_models
# }
def all_cars(request):
    cars = Car.objects.all()
    return render(request,'cars/all_cars.html',{'cars':cars})

def car(request):
    return HttpResponse('My cars')

def info(request):
    return HttpResponse('Info about cars')

def main(request):
    return render(request, 'cars/index.html', {'cars': lst_car})

def bmw(request):
    return render(request, 'cars/BMW.html', {'cars': lst_car})
def volvo(request):
    return render(request, 'cars/VOLVO.html', {'cars': lst_car})
def tesla(request):
    return render(request,'cars/tesla.html',{'cars':lst_car})

def year_create(request,model):
    if model>2022:
        return redirect('index')
    return HttpResponse(f'year {model}')

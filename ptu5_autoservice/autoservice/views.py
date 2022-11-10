from django.shortcuts import render
from django.http import HttpResponse
from . models import CarModel, Car, Service, Order, OrderLine

# Create your views here.

def index(request):
    # return HttpResponse("Testing")
    name_count = Service.objects.count()
    order_count = Order.objects.count()
    car_count = Car.objects.count()

    context = {
        'name_count': name_count,
        'car_count': car_count,
        'order_count': order_count
    }

    return render(request, 'autoservice/index.html', context=context)

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from . models import CarModel, Car, Service, Order, OrderLine
from django.views.generic import ListView, DetailView
from django.core.paginator import Paginator

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

def cars(request):
    paginator = Paginator(Order.objects.all(), 2)
    page_number = request.GET.get('page')
    paged_cars = paginator.get_page(page_number)
    return render(request, 'autoservice/cars.html', {'cars': paged_cars}) #{'cars': Car.objects.all()}) #

def car(request, car_id):
    return render(request, 'autoservice/car.html', {'car':get_object_or_404(Car, id = car_id)})

class OrderListView(ListView):
    model = Order
    paginate_by = 1
    template_name ='autoservice/orders_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['order_count'] = self.get_queryset().count()
        return context

class OrderDetailView(DetailView):
    model = Order
    template_name ='autoservice/order_detail.html'






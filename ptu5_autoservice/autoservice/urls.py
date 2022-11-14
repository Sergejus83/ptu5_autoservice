from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('cars/', views.cars, name='cars'),
    path('car/<int:car_id>/', views.car, name='car'),
    path('orders/', views.OrderListView.as_view(), name='orders'),
    path('order/<int:pk>', views.OrderDetailView.as_view(), name='order'),
]

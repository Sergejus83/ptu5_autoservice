from django.contrib import admin
from . import models
# Register your models here.

class OrderLineInline(admin.TabularInline):
    model = models.OrderLine
    # extra = 0
    # readonly_fields = ('order_id', )
    # can_delete = False

class OrderLineAdmin(admin.ModelAdmin):
    list_display = ('service', 'quantity', 'price', 'total', 'order')
    ordering = ('order', 'id',)
    list_filter = ('order',)


class OrderAdmin(admin.ModelAdmin):
    list_display = ('car', 'date')
    ordering = ('date',)
    list_filter = ('car',)
    inlines = (OrderLineInline,)


class CarAdmin(admin.ModelAdmin):
    list_display = ('client', 'car_model', 'plate', 'vin')
    ordering = ('car_model',)
    list_filter = ('client', 'car_model',)
    search_fields = ('plate', 'vin',)


class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')
    ordering = ('name',)
    list_filter = ('name',)


admin.site.register(models.Car, CarAdmin)
admin.site.register(models.CarModel)
admin.site.register(models.Service, ServiceAdmin)
admin.site.register(models.Order, OrderAdmin)
admin.site.register(models.OrderLine, OrderLineAdmin)
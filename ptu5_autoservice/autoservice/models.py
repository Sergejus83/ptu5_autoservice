from django.db import models
from django.utils.translation import gettext_lazy as _ # galima palikti su "_" - nebus klaidos
from datetime import date

# Create your models here.
class CarModel(models.Model):
    YEARS_CHOICES = ((years, str(years)) for years in reversed(range(1900, date.today().year+1))) 
    # tai nera kintamasis (didziosem raidems) - tai funkcija, papildoma eilute nesusikuria

    make = models.CharField(_("make"), max_length=50)
    model = models.CharField(_("model"), max_length=50)
    year = models.IntegerField(_("year"), choices = YEARS_CHOICES)
    engine = models.CharField(_("engine"), max_length=50)

    def __str__(self) -> str:
        return f"{self.make} {self.model} ({self.year}), {self.engine}"


class Car(models.Model):
    car_model = models.ForeignKey(CarModel, verbose_name=_("car_model"), on_delete=models.CASCADE, related_name='cars',)
    plate = models.CharField(_("license plate"), max_length=15)
    vin = models.CharField(_("VIN code"), max_length=50)
    client = models.CharField(_("client name"), max_length=150)

    def __str__(self) -> str:
        return f"{self.car_model.make} {self.car_model.model} {self.plate} {self.client}"


class Service(models.Model):
    name = models.CharField(_("name"), max_length=100)
    price = models.DecimalField(_("price"), max_digits=20, decimal_places=2)

    def __str__(self) -> str:
        return self.name


class Order(models.Model):
    car = models.ForeignKey(Car, verbose_name=_("car"), on_delete=models.CASCADE, related_name='orders',)
    total = models.DecimalField(_("total"), max_digits=20, decimal_places=2, default=0)
    date = models.DateField(_("date"), auto_now_add=True)

    def get_total(self):
        total = 0
        for line in self.order_lines.all():
            total += line.total
            return total

    def save(self,*args, **kwargs):
        if not self._state.adding:
            self.total = self.get_total()
            super().save(*args, **kwargs)


    def __str__(self) -> str:
        return f"{self.date}: {self.total}"


class OrderLine(models.Model):
    order = models.ForeignKey(Order, verbose_name=_("order"), on_delete=models.CASCADE, related_name = 'order_lines', )
    service = models.ForeignKey(Service, verbose_name=_("service"), on_delete=models.CASCADE, related_name='order_lines',)
    quantity = models.IntegerField(_("quantity"), default=1)
    price = models.DecimalField(_("price"), max_digits=20, decimal_places=2)

    @property
    def total(self):
        return self.quantity * self.price

    def __str__(self) -> str:
        return f"{self.service.name}: {self.quantity} x {self.price}"


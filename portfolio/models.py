from django.contrib.auth import get_user_model
from django.db import models
from django.db.models import Q
from django.utils import timezone
import requests
from users.models import CustomUser


class Customer(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE,)
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    cust_number = models.IntegerField(blank=False, null=False)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=10)
    email = models.EmailField(max_length=200)
    cell_phone = models.CharField(max_length=50)
    created_date = models.DateTimeField(
        default=timezone.now)
    updated_date = models.DateTimeField(auto_now_add=True)

    def created(self):
        self.created_date = timezone.now()
        self.save()

    def updated(self):
        self.updated_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.user)

# Create your models here.
class Investment(models.Model):
    user = models.ForeignKey(Customer, on_delete=models.CASCADE,related_name='investment')
    category = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    acquired_value = models.DecimalField(max_digits=10, decimal_places=2)
    acquired_date = models.DateField(default=timezone.now)
    recent_value = models.DecimalField(max_digits=10, decimal_places=2)
    recent_date = models.DateField(default=timezone.now, blank=True, null=True)

    def created(self):
        self.acquired_date = timezone.now()
        self.save()

    def updated(self):
        self.recent_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.user)

    def results_by_investment(self):
        return self.recent_value - self.acquired_value

class Stock(models.Model):
    user = models.ForeignKey(Customer, on_delete=models.CASCADE,related_name='stock')
    symbol = models.CharField(max_length=10)
    name = models.CharField(max_length=50)
    shares = models.DecimalField (max_digits=10, decimal_places=1)
    purchase_price = models.DecimalField(max_digits=10, decimal_places=2)
    purchase_date = models.DateField(default=timezone.now, blank=True, null=True)

    def created(self):
        self.recent_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.user)

    def current_stock_price(self):
        json_data = {}
        symbol_f = str(self.symbol)
        main_api = 'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&amp;symbol='
        api_key = '&interval=1min&apikey= AH1BJBJQ6QI8EGJ4'
        url = main_api + symbol_f + api_key
        json_data = requests.get(url).json()
        open_price = float(json_data["Global Quote"]["02. open"])
        share_value = open_price
        return share_value

    def current_stock_value(self):
        return float(self.current_stock_price()) * float(self.shares)

    def initial_stock_value(self):
        return self.shares * self.purchase_price


    def final_result(self):
        return float(self.current_stock_value()) - float(self.initial_stock_value())

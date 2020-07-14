from django.contrib import admin
from .models import Customer, Investment, Stock


class CustomerList(admin.ModelAdmin):
    list_display = ('cust_number', 'name', 'city', 'cell_phone')
    list_filter = ('cust_number', 'name', 'city')
    search_fields = ('cust_number', 'name')
    ordering = ['cust_number']


class InvestmentList(admin.ModelAdmin):
    list_display = ('user', 'category', 'description', 'recent_value')
    list_filter = ('user', 'category')
    search_fields = ('user', 'category')
    ordering = ['user']

class StockList(admin.ModelAdmin):
    list_display = ('user','symbol', 'name', 'shares', 'purchase_price')
    list_filter = ('user','symbol', 'name')
    search_fields = ('user','symbol', 'name')
    ordering = ['user']

admin.site.register(Customer,CustomerList)
admin.site.register(Investment, InvestmentList)
admin.site.register(Stock, StockList)



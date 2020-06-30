from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic

from .models import *
from .forms import *

@login_required
def customer_list(request):
    counter = 0
    customer = Customer.objects.all()
    return render(request, 'portfolio/customer_list.html',{'customer' :customer})

@login_required
def customer_edit(request, pk):
   customer = get_object_or_404(Customer, pk=pk)
   if request.method == "POST":
       form = CustomerForm(request.POST, instance=customer)
       if form.is_valid():
           customerform = form.save(commit=False)
           customerform.save()
           messages.success(request, f'Your Customer has been updated')
           return redirect('/customer_list/')

   else:
       # edit
       customerform = CustomerForm(instance=customer)
   return render(request, 'portfolio/customer_edit.html', {'customerform': customerform})

@login_required
def customer_delete(request, pk):
   customer = get_object_or_404(Customer, pk=pk)
   customer.delete()
   return redirect('/customer_list/')

def home(request):
   return render(request, 'portfolio/home.html',
                 {'portfolio': home})


def stock_list(request):
    stock = Stock.objects.all()
    return render(request, 'portfolio/stock_list.html', {'stock':stock})


def stock_edit(request, pk):
    stock = get_object_or_404(Stock,pk = pk)
    if request.method == 'POST':
        form = StockForm(request.POST, instance = stock)
        if form.is_valid():
            stockform = form.save(commit=False)
            stockform.save()
            messages.success(request, f'Your Customer has been updated')
            return redirect('/stock_list/')

    else:
            # edit
        stockform = StockForm(instance=stock)
        return render(request, 'portfolio/stock_edit.html', {'stockform': stockform})


def stock_new(request):
    if request.method == 'POST':
        form = StockForm(request.POST)
        if form.is_valid():
            stock = form.save(commit=False)
            stock.created_date = timezone.now()
            stock.save()
            messages.success(request, f'Your New Board has been updated')
            return redirect('/stock_list/')

    else:
            # edit
        stockform = StockForm()
        return render(request, 'portfolio/stock_new.html', {'stockform': stockform})


@login_required
def stock_delete(request, pk):
   stock = get_object_or_404(Stock, pk=pk)
   stock.delete()
   return redirect('/stock_list/')


def investment_list(request):
    investment = Investment.objects.all()
    return render(request, 'portfolio/investment_list.html', {'investment':investment})


def investment_edit(request, pk):
    investment = get_object_or_404(Investment,pk = pk)
    if request.method == 'POST':
        form = InvestmentForm(request.POST, instance = investment)
        if form.is_valid():
            investmentform = form.save(commit=False)
            investmentform.save()
            messages.success(request, f'Your Customer has been updated')
            return redirect('/investment_list/')

    else:
            # edit
        investmentform = InvestmentForm(instance=investment)
        return render(request, 'portfolio/investment_edit.html', {'investmentform': investmentform})


def investment_new(request):
    if request.method == 'POST':
        form = InvestmentForm(request.POST)
        if form.is_valid():
            investmentform = form.save(commit=False)
            investmentform.created_date = timezone.now()
            investmentform.save()
            messages.success(request, f'Your New Board has been updated')
            return redirect('/investment_list/')

    else:
            # edit
        investmentform = InvestmentForm()
        return render(request, 'portfolio/investment_new.html', {'investmentform': investmentform})


@login_required
def investment_delete(request, pk):
   investment = get_object_or_404(Investment, pk=pk)
   investment.delete()
   return redirect('/investment_list/')

@login_required
def portfolio_list(request, pk):
    customer = get_object_or_404(Customer,pk=pk)
    stock = Stock.objects.filter(customer=customer)
    return render(request,'portfolio/portfolio_list.html',{'stock':stock})


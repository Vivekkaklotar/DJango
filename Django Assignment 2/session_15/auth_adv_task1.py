# views.py
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required(login_url='/accounts/login/')
def my_orders_view(request):
    orders = request.user.orders.all()
    return render(request, 'orders/my_orders.html', {'orders': orders})
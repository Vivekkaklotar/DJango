# views.py
from django.shortcuts import redirect

def dashboard_redirect(request):
    user = request.user
    if user.groups.filter(name='Seller').exists():
        return redirect('seller_dashboard')
    elif user.groups.filter(name='Buyer').exists():
        return redirect('buyer_dashboard')
    else:
        return redirect('default_dashboard')
# views.py
from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render, HttpResponse

@login_required
def post_product_view(request):
    # Check if user has 'Seller' group
    if not request.user.groups.filter(name='Seller').exists():
        return HttpResponse("Access Denied: Only Sellers can post products!", status=403)
        
    return render(request, 'seller/post_product.html')
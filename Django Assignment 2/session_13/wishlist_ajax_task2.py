# views.py
from django.http import JsonResponse

def remove_wishlist(request, product_id):
    if request.method == 'DELETE':
        # Remove item from wishlist model/session
        return JsonResponse({'status': 'success', 'message': 'Product removed from wishlist'})
    return JsonResponse({'status': 'error'}, status=400)
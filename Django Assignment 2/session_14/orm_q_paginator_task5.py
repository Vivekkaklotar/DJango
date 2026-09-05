from django.db.models import Q
from django.core.paginator import Paginator
from products.models import Product

# Complex Q filter (Electronics OR price < 1000)
queryset = Product.objects.filter(Q(category='Electronics') | Q(price__lt=1000))

# Paginate (5 items per page)
paginator = Paginator(queryset, 5)
page_1 = paginator.get_page(1)

for product in page_1:
    print(f"{product.name} - ₹{product.price}")
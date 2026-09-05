# Efficient single SQL JOIN query
products = Product.objects.select_related('category').all()
for p in products:
    print(f"Product: {p.name} | Category: {p.category.name}")
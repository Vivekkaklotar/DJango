# Querying Chinese restaurants rated > 4
chinese_top = Restaurant.objects.filter(cuisine__name='Chinese', rating__gt=4.0)
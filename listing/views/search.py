from django.views import View
from django.shortcuts import redirect, render
from vendor.models import Product
from django.db.models import Q

class Search(View):
    def get(self, request):
        keywords = request.GET.get('search_value')

        products_list = Product.objects.filter(
            Q(title__icontains=keywords) | 
            Q(category__name__icontains=keywords) |
            Q(address__icontains=keywords) |
            Q(mrp__icontains=keywords) |
            Q(price__icontains=keywords) |
            Q(size__icontains=keywords) |
            Q(size_unit__unit_name__icontains=keywords) |
            Q(owner__first_name__icontains=keywords) |
            Q(owner__last_name__icontains=keywords) |
            Q(brand__icontains=keywords) |
            Q(description__icontains=keywords) |
            Q(state__icontains=keywords)
        )

        context = {
            'products' : products_list,
            'keywords' : keywords,
            'total' : len(products_list),
        }
        return render(request, 'search.html', context)

    def post(self, request):
        return ''
from django.views import View
from django.shortcuts import redirect, render
from vendor.models import Product, Image, Bullet_point
from django.contrib import messages
from django.db.models import Q


class Single(View):
    def get(self, request, pid):
        # Get product by pid
        product = Product.objects.all().filter(id=pid).first()
        if product:
            images = Image.objects.all().filter(product=product)
            products = Product.objects.filter(Q(district = product.district), ~Q(id = product.id))
            bullet_point = Bullet_point.objects.filter(product=product)
            context = {
                'product' : product,
                'images' : images,
                'products' : products,
                'bps' : bullet_point,
            }
            return render(request, 'single.html', context)

        else:
            return messages.error(request, 'Product not found.')

    def post(self, request):
        return render(request, 'single.html')
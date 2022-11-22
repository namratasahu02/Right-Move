from email.mime import image
from re import I
from django.views import View
from django.shortcuts import redirect, render
from vendor.models import Product
from listing.models import Banner
from blog.models import Blog


class Home(View):
    def get(self, request):
        products = Product.objects.all()
        ad_products = Product.objects.all().filter(highlighted=True)
        banners = Banner.objects.all().filter(set_show=True)[:4]
        banner2 = Banner.objects.all().filter(set_as_banner_2=True).last()
        blogs = Blog.objects.all()[:5]
        
        context = {
            'products' : products, 
            'banners':banners, 
            'banner2':banner2, 
            'ad_products':ad_products,
            'blogs' : blogs,
        }
        return render(request, 'home.html', context)

    def post(self, request):
        pass
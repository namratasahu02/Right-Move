from django.views import View
from django.shortcuts import render, redirect
from vendor.models import Product
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages

class Dashboard(LoginRequiredMixin, View):
    def get(self, request):
        context = {
            'products' : Product.objects.all().filter(owner=request.user),
        }
        return render(request, 'dashboard.html', context)

    def post(self, request):
        pid = request.POST.get('pid')
        print(pid, '\n\n')
        p = Product.objects.all().filter(id=pid)

        if p:
            p.delete()
            messages.success(request, f'Product {pid} successfully deleted.')

        else:
            messages.error(request, 'Product not found to delete.')
        return redirect('dashboard')
from django.urls import path 
from .views import Add_product, Dashboard, Edit_product

urlpatterns = [
    path('', Dashboard.as_view(), name='dashboard'),
    path('add', Add_product.as_view(), name='add'),
    path(r'edit/<int:pid>', Edit_product.as_view(), name='edit'),
]
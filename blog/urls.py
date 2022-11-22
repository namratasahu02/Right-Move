from django.urls import path 
from .views import Read_blog

urlpatterns = [
    path(r'<int:bid>', Read_blog.as_view(), name='read_blog'),
]
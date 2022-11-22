from django.shortcuts import render
from django.views import View
from .models import Blog
class Read_blog(View):
    def get(self, request, bid):
        blog = Blog.objects.all().filter(id=bid).first()
        return render(request, 'blog.html', {'blog':blog})

    def post(self, request):
        pass
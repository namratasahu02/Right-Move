from django.urls import path 
from listing.views import Home, Single, Search


urlpatterns = [
    path('', Home.as_view(), name='homepage'),
    path(r'listing/<int:pid>', Single.as_view(), name='single'),
    path('search', Search.as_view(), name='search'),
]
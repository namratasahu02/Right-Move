from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', include('listing.urls')),
    path('admin/', admin.site.urls),
    path('authenticaion/', include('authentication.urls')),
    path('vendor/', include('vendor.urls')),
    path('blog/', include('blog.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


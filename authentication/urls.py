from django.urls import path 
from .view import Registration, Verification, Login, Logout, Recover

urlpatterns = [
    path('registration', Registration.as_view(), name="registration"),
    path('verification', Verification.as_view(), name="verification"),
    path('login', Login.as_view(), name="login"),
    path('logout', Logout.as_view(), name="logout"),
    path('recover', Recover.as_view(), name="recover"),
]
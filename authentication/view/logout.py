from django.contrib.auth import logout
from django.views import View
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin


class Logout(LoginRequiredMixin, View):
    def get(self, request):
        logout(request)
        messages.warning(request, "You are loged out, Please login to you account.")
        return redirect('login')
import re
from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib import messages
from django.db.models import Q


class Login(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        context = {'email' : email}
        
        user = User.objects.all().filter(username=email).first()

        print('\n\n\n', user, '\n\n\n')

        if user:
            if user.is_active:
                v_user = authenticate(username=email, password=password)

                if v_user:
                    login(request, v_user)
                    messages.success(request, 'You have been successfully logged in.')
                    return redirect('homepage')

                else:
                    messages.error(request, 'Invalid password')
                    return render(request, 'login.html', context)
            
            else:
                request.session['uid'] = user.id
                messages.error(request, "Your account is not verified. Please verify your account")
                return redirect('verification')

        else:
            messages.error(request, 'Invalid Email address')
            return render(request, 'login.html', context)
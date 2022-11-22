from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from authentication.models.user_data import User_data


class Recover(View):
    def get(self, request):
        return render(request, 'recover.html')

    def post(self, request):
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        
        if password1 == password2:
            user = User.objects.all().filter(username = email)

            if user:
                user_data = User_data.objects.all().filter(user = user[0])

                if user_data:
                    user_data.update(password = password1)
                    request.session['uid'] = user[0].id
                    return redirect('verification')

            else:
                messages.error(request, 'Account not found.')

        else:
            messages.error(request, 'Password not matched.')

        return redirect('recover')
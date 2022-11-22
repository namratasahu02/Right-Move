from django.shortcuts import redirect, render
from django.views import View
from django.contrib.auth.models import User
from authentication.models import User_data, Error_log
from django.contrib import messages


class Registration(View):
    def get(self, request):
        return render(request, 'registration.html')

    def post(self, request):
        # Get data from form
        f_name = request.POST.get('fname')
        l_name = request.POST.get('lname')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        gender = request.POST.get('gender')
        phone = request.POST.get('phone')
        gstin  = request.POST.get('gstin')
        aadhaar  = request.FILES.get('aadhaar')
        username = email
        error_user = error_code = error = None
        context = {
            'f_name' : f_name,
            'l_name' : l_name,
            'email' : email,
            'gender' : gender,
            'phone' : phone,
            'gstin' : gstin,
            'aadhaar' : aadhaar,
        }

        # __ Check form data __

        # required fields
        if f_name and l_name and email and password1 and password2 and gender and phone:
            if password1 == password2 :
                ex_user = User.objects.all().filter(email = email)
                if not ex_user:
                    try:
                        newUser = User.objects.create_user(username=username, email=email, password=password1, first_name=f_name, last_name=l_name)
                        newUser.is_active = False
                        newUser.save()
                        try:
                            user_data = User_data(user=newUser, phone=phone, gstin=gstin, gender=gender, aadhaar = aadhaar)
                            user_data.save()
                            request.session['uid'] = newUser.id
                            request.session['v_type'] = 'registration'
                            return redirect('verification')
                        except:
                            error = 'Enable to save user data. Please try again.'
                            error_code = '02x005'
                            error_user = newUser
                            newUser.delete()
                            messages.error(request, error)
                    except:
                        error = 'Enable to create account, please try again.'
                        error_code = '02x004'
                        messages.error(request, error)
                else:
                    error_user = ex_user[0]
                    error = 'This email is already registered'
                    error_code = '02u003'
                    messages.error(request, error)
            else:
                error = 'Password not matched'
                error_code = '02u002'
                messages.error(request, error)
        else:
            error = 'Form data is corrupted :)'
            error_code = '02x001'
            messages.error(request, error)

        if error and error_code:
            if error_user:
                Error_log(user=error_user, error_code=error_code, error=error).save()

            else:
                Error_log(error_code=error_code, error=error).save()

        # if error return form data
        return render(request, 'registration.html', context)
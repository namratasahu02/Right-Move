from django.shortcuts import redirect, render
from django.views import View
from django.contrib.auth.models import User
import math, random
from django.core.mail import send_mail
from authentication.models import User_data
from django.contrib import messages
from django.contrib.auth import login


class Verification(View):
    def get(self, request):
        user_list = self.find_user(request)

        if user_list:
            user = user_list[0]
            user_data = user_list[1]
            email = user.email
            otp = self.send_otp(email)

            if otp:
                user_data.update(otp=otp)
                messages.success(request, 'OTP send succesfully. Please check you email.')
                return render(request, 'verification.html')

            else:
                messages.error(request, 'Can not send otp at this time.') 

        else:
            messages.error(request, 'Enable to find your account.')

        return redirect('homepage')


    def post(self, request):
        userOTP = request.POST.get('otp')
        user, user_data = self.find_user(request) 

        if user and user_data:
            otp = user_data[0].otp

            if otp == userOTP:
                newPass = user_data[0].password

                if newPass:
                    user.set_password(newPass)
                    user_data.update(password = None)

                # Activate user account
                user.is_active = True 
                user.save()
                request.session['uid'] = None 

                # Automatic login
                if login(request, user):
                    messages.success(request, 'Your account successfully created.') 
                    return redirect('homepage')

                messages.error(request, 'Failed to automatic login. Please login manually') 
                return redirect('login')
            else:
                messages.error(request, 'Invalid otp.')
        else:
            messages.error(request, 'Enable to find your account.')

        return render(request, 'verification.html')


    def generateOTP(self) :
        digits = "0123456789"
        OTP = ""
        for i in range(4) :
            OTP += digits[math.floor(random.random() * 10)]
        return OTP


    def send_otp(self, email):
        otp =self.generateOTP()
        htmlgen = f'''
            Dear customer, <br>
            Thank You for registering with us❤️
            <br> <br>
            Enter the below mentioned one time password to complete your registration.
            <br>
            <h2 style="background-color: antiquewhite; text-align: center; padding: 8px 0; width: 100px;
            border: 1px solid silver;">
                {otp}
            </h2>
            <br>
            <small>
                Please do not share your OTP with anyone
            </small>
        '''

        if send_mail('Account verification',otp,'no-reply@kestatevision.com',[email], fail_silently=False, html_message=htmlgen):
            return otp

        return False


    def find_user(self, request):
        uid = request.session.get('uid')
        if uid:
            user = User.objects.all().filter(id=int(uid)).first()
            user_data = User_data.objects.all().filter(user = user)
            return [user, user_data]

        return False 
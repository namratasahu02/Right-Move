Author : Namrata sahu
Date : 10/02/2022

=========================================================================
Apps List                                                                
-------------------------------------------------------------------------
                                                                         
1. authentication (Login, Logout, New account, reset password)           
2. configuration (Category, size, state, status)                          
3. listing (Home, view, contact)
4. vendor (List, delete, edit)

=========================================================================





















Application id = 02
--------------------

How to use this application
===========================

1. Match and modify media and static folder of you project
2. import os and Copy line number 90 - 115 from setting.py and paste it in your project's setting.py
3. Copy line 3, 4, 9, 10 from MAIN/urls.py
4. copy App folder (Authentication/Authentication) and paste in you project 
5. Add app name in you settings.py > INSTALLED_APPS 
6. Home page urls name must be 'homepage'
7. Copy & past file /Static/sass/_authentication.scss and register it in main.scss 


Error Codes
===========

Example = 0 2 x 0 0 1
Error code lenght = 6
1st & 2nd degits = application id ( Authentication app id = 02)
3rd degits = Error type
last 3 degits = Error id 


Error Types
===========

1. Eare Error = Not well known error (Ex: Someone trying to menuplate the form data)
         unit = x

2. Usual error = Normal error (Ex: Faild to redirect)
         unit = u

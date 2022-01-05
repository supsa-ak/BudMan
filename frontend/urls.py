from django.urls import path
# from django.contrib.auth.views import LogoutView
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('login', loginPage, name='login'),
    path('signup', signupPage, name='signup'),
    path('logout', logoutUser),
    # path('privacy-policy', ),
    # path('terms-of-service', ),
]
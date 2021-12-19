from django.urls import path

from .views import *
urlpatterns = [
    path('', home, name='home'),
    path('login', loginPage, name='login'),
    path('logout', logoutUser),
]
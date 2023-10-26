from django.urls import path
from . import views

urlpatterns = [
    path('login/',views.Application,name='login'),
    path('login/passwordpage/',views.feedbackpagepass,name='pass'),
    path('login/passwordpage/main/',views.feedbackpage,name='main'),
    path('login/passwordpage/main/thankyou/',views.thankyou,name='thank'),


	]
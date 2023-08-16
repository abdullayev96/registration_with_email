from django.urls import path
from .views import RegisterAPI, VerifyEmailAPI


urlpatterns  = [
          path('register/',RegisterAPI.as_view(), name = 'register'),
          path('email-verify/', VerifyEmailAPI.as_view(), name = 'email-verify')
]
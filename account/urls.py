from django.urls import path
from .views import EmailAPI



urlpatterns  = [
          path('email/', EmailAPI.as_view())
]
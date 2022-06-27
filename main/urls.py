from django.urls import path
from main.views import register_request
app_name = "main"

urlpatterns = [
    path("", register_request, name='register')  # /register/
]
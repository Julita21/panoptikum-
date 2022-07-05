from django.urls import path
from main.views import register_request, homepage, login_request, logout_request, user_profile

app_name = "main"

urlpatterns = [
    path("", homepage, name="homepage"),                    # /
    path("register/", register_request, name='register'),   # /register/
    path("login/", login_request, name='login'),            # /login/
    path("logout/", logout_request, name='logout'),         # /logout/
    path("user/<int:id>/userprofile/", user_profile, name="userprofile")  # /user/1/userprofile/

]


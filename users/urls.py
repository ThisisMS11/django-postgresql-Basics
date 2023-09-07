from django.urls import path
from users.views import CustomUserRegisterView

# this value has to be equal to namespace that you provided in backends/urls 
app_name="users"

urlpatterns = [
    path("register/", CustomUserRegisterView.as_view(), name="register"),
]

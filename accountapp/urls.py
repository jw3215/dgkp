from django.contrib.auth.views import LoginView, LogoutView
from accountapp.views import AccountCreateView, AccountDetailView, hello_world
from django.urls.conf import path

# from django.contrib.auth.views import LoginView

app_name = "account_app"

urlpatterns = [
    path("hello_world/", hello_world, name="hello_world"),
    path(
        "login/", LoginView.as_view(template_name="accountapp/login.html"), name="login"
    ),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("create/", AccountCreateView.as_view(), name="create"),
    path("detail/<int:pk>", AccountDetailView.as_view(), name="detail"),
]

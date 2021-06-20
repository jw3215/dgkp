from functools import partial
from subscribeapp.apps import SubscribeappConfig
from subscribeapp.views import SubscriptionView
from django.urls import path

app_name = "subscribeapp"
urlpatterns = [path("subscribe/", SubscriptionView.as_view(), name="subscribe")]

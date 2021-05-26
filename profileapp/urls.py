from profileapp.views import ProfileCreateView
from django.urls.conf import path


app_name = "profileapp"

urlpatterns = [
    path("create/", ProfileCreateView.as_view(), name="create"),
]

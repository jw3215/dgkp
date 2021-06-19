from commentapp.views import CommentCreateView
from django.urls.conf import path

app_name = "commentapp"

urlpatterns = [path("create/", CommentCreateView.as_view(), name="create")]

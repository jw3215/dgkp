from django.contrib.auth.models import User
from django.http.response import HttpResponseForbidden
from profileapp.models import Profile


def profile_ownership_required(func):
    def decorated(request, *args, **kwargs):
        profile = Profile.objects.get(pk=kwargs["pk"])
        if not profile == request.profile:
            return HttpResponseForbidden()
        return func(request, *args, **kwargs)

    return decorated
from django.urls.base import reverse
from accountapp.models import HelloWorld
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, resolve_url


def hello_world(request):
    if request.method == "POST":
        temp = request.POST.get("hello_world_input")

        new_hello_world = HelloWorld()
        new_hello_world.text = temp
        new_hello_world.save()

        hello_world_list = HelloWorld.objects.all()
        return HttpResponseRedirect(reverse("accountapp:hello_world"))
        # return render(
        #     request,
        #     "accountapp/hello_world.html",
        #     context={
        #         "hello_world_output": new_hello_world,
        #         "hello_world_list": hello_world_list,
        #     },
        # )
    else:
        hello_world_list = HelloWorld.objects.all()

        return render(
            request,
            "accountapp/hello_world.html",
            context={"text": "GET METHOD!!!", "hello_world_list": hello_world_list,},
        )

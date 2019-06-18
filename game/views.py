from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect


def index(request):
    # return HttpResponse("Hello, world. You're at the polls index.")
    print("I'm in Index")
    return render(request,"game/index.html")
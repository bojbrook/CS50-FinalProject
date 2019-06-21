from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect

from .models import game, studio, Platform

from datetime import timedelta, datetime, date

def index(request):
    try:
        games = game.objects.all().order_by("release_date")
    except game.DoesNotExist:
        return HttpResponse("No Games")

    game_info_arr = []
    for g in games:
        # date = 
        # t = timedelta(g.release_date)
        x = date.today()
        delta = abs((g.release_date - x))
        # if(delta.days > )

        # current = datetime(g.release_date.year,g.release_date.month,g.release_date.day)
        # t = timedelta(current)
        print(f"Current Time {x} ")
        print(f"Delta Time {delta}")
        game_info = {
            "id":           g.id,
            "title":        g.title,
            "studio":       g.studio,
            "cover":        g.cover_url,
            "days_until":   abs((g.release_date - x).days)
        }
        game_info_arr.append(game_info)

    print(game_info_arr)
    context = {
        'games': game_info_arr
    }
    return render(request,"game/index.html", context)


def game_view(request, game_id):
    try:
        title = game.objects.get(pk=game_id)
    except game.DoesNotExist:
        return HttpResponseRedirect(reverse("index"))

    context = {
        'game': title
    }
    return render(request,"game/game_info.html", context)

def studios_view(request):
    try:
        studios = studio.objects.all()
    except studio.DoesNotExist:
        return HttpResponseRedirect(reverse("index"))

    context = {
        "studios": studios
    }
    return render(request,"game/studios.html", context)

def platforms_view(request):
    try:
        platforms = Platform.objects.all()
    except studio.DoesNotExist:
        return HttpResponseRedirect(reverse("index"))

    context = {
        "platforms": platforms
    }
    return render(request,"game/platforms.html", context)
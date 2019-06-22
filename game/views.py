from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect

from .models import game, studio, Platform

from datetime import timedelta, datetime, date

# returns all of the game data 
def generate_game_data(games):
    game_info_arr = []
    for g in games:
        x = date.today()
        delta = abs((g.release_date - x))
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
    return game_info_arr

def index(request):
    try:
        games = game.objects.all().order_by("release_date")
    except game.DoesNotExist:
        return HttpResponse("No Games")

    game_info_arr = generate_game_data(games)
    context = {
        'games': game_info_arr
    }
    return render(request,"game/index.html", context)


# View for an individual game
def game_view(request, game_id):
    try:
        title = game.objects.get(pk=game_id)
    except game.DoesNotExist:
        return HttpResponseRedirect(reverse("index"))

    context = {
        'game': title
    }
    return render(request,"game/game_info.html", context)

# A view of all of the studios
def studios_view(request):
    try:
        studios = studio.objects.all()
    except studio.DoesNotExist:
        return HttpResponseRedirect(reverse("index"))
    studios_arr = []
    for Studio in studios:
        info = {
            "name":     Studio.name,
            "url_name": Studio.name.replace(" ","_")
        }
        studios_arr.append(info)

    print(studios_arr)
    context = {
        "studios": studios_arr
    }
    return render(request,"game/studios.html", context)

# A view for each individual studio and all of their games
def studio_info_view(request, studio_name):
    studio_id = studio_name.replace("_"," ")
    try:
        Studio = studio.objects.get(pk=studio_id)
        studio_games = game.objects.filter(studio=Studio).order_by("release_date")
    except studio.DoesNotExist:
        return HttpResponseRedirect(reverse("index"))
    except game.DoesNotExist:
        return HttpResponseRedirect(reverse("index"))

    context = {
        "studio":   Studio,
        "games":    generate_game_data(studio_games)
    }
    return render(request,"game/studio_info.html",context)

# A view for all of the platforms
def platforms_view(request):
    try:
        platforms = Platform.objects.all()
    except studio.DoesNotExist:
        return HttpResponseRedirect(reverse("index"))

    context = {
        "platforms": platforms
    }
    return render(request,"game/platforms.html", context)

def platform_info_view(request, platform_id):
    try:
        platform = Platform.objects.get(pk=platform_id)
        platform_games = game.objects.filter(Platform=platform).order_by("release_date")
    except studio.DoesNotExist:
        return HttpResponseRedirect(reverse("index"))
    context = {
        "platform": platform,
        "games":    generate_game_data(platform_games)
    }
    return render(request,"game/platform_info.html", context)
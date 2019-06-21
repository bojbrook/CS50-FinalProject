from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('game/<int:game_id>', views.game_view, name='game_view'),

    path('studios/', views.studios_view, name='studios_view'),

    path('platforms/', views.platforms_view, name='platforms_view'),
]
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('game/<int:game_id>', views.game_view, name='game_view'),

    path('studios/', views.studios_view, name='studios_view'),
    path('studios/<slug:studio_name>', views.studio_info_view, name='studio_info_view'),

    path('platforms/', views.platforms_view, name='platforms_view'),
    path('platforms/<int:platform_id>', views.platform_info_view, name='platform_info_view')
]
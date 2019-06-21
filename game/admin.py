from django.contrib import admin
from .models import studio, game, Platform
# Register your models here.
admin.site.register(studio)
admin.site.register(game)
admin.site.register(Platform)
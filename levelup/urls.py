from django.contrib import admin
from django.conf.urls import include
from django.urls import path
from levelupapi.views import register_user, login_user
from django.conf.urls import include
from rest_framework import routers
from levelupapi.views import GenreView
from levelupapi.views import GameView
from levelupapi.views import EventView


router = routers.DefaultRouter(trailing_slash=False)
router.register(r'genres', GenreView, 'genre')
router.register(r'games', GameView, 'game')
router.register(r'events', EventView, 'event')

urlpatterns = [
    path('register', register_user),
    path('login', login_user),
    path('admin/', admin.site.urls),
    path('', include(router.urls))
]


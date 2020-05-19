from django.urls import path
from . import views

app_name = 'web'
urlpatterns = [
    # Global paths -->
    path('', views.home, name='home'),
    path('search', views.search, name='search'),
    path('$/help', views.help, name='help'),
    path('$/discover', views.discover, name='discover'),
    path('$/top', views.top, name='top'),

    # User related paths. To be created an User app later -->
    path('$/wallet', views.wallet, name='wallet'),
    path('$/publish', views.publish, name='publish'),
    path('$/published', views.published, name='published'),
    path('$/channels', views.channels, name='channels'),
    path('$/dashboard', views.dashboard, name='dashboard'),
    path('$/rewards', views.rewards, name='rewards'),
    path('$/invite', views.invite, name='invite'),
    path('$/settings', views.settings, name='settings'),
    path('$/tags', views.tags, name='tags'),
    path('$/following', views.following, name='following'),

    # Resolve paths -->
    path('<str:name>', views.resolve, name='community'),
    path('<str:name>#<str:claim_id>', views.resolve, name='permanent'),
    path('<str:channel_name>/<str:name>', views.resolve, name='signed'),

]


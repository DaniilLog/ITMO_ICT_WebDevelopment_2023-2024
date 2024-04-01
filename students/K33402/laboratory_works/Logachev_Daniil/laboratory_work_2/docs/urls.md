```python
from django.contrib.auth import views as auth_views
from django.contrib import admin
from django.urls import path

from .views import (
    game_detail,
    gamer_registration,
    gamer_unregistration,
)

from .views import *

urlpatterns = [
    path('meeting/<int:game_id>/', game_detail, name='game_detail'),
    path('meeting/<int:game_id>/register/', gamer_registration, name='gamer_registration'),
    path('meeting/<int:game_id>/unregister/', gamer_unregistration, name='gamer_unregistration'),
    path("admin/", admin.site.urls),
    path("", base, name="base"),
    path("login/", auth_views.LoginView.as_view(template_name="login.html"), name="login"),
    path('logout/', user_logout, name='logout'),
    path("register/", user_register, name="register_user"),
    path("profile/", profile, name="profile"),
    path("meeting/", tablo, name="tablo"),
    path("meeting/<int:game_id>/comments/", comments, name="comments"),
    path('all_game_results/', all_game_results, name='all_game_results'),
]
```
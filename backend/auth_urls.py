from django.urls import path
from users.views import simple_login, current_user

urlpatterns = [
    path('simple-login/', simple_login, name='simple-login'),
    path('current/', current_user, name='current-user'),
]
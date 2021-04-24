from django.urls import path
from django_102.views import *

urlpatterns = [
    path('', index),
    path('2/', UsersListView.as_view()),
    path('games/', GamesListView.as_view()),
    path('test/', test_view),
    path('method/', method_req),
]

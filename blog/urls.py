from django.urls import path
from . import views


urlpatterns = [
    path('', views.main, name='main'),
    path('post', views.post_list, name='post_list'),
]

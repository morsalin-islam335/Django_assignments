from django.urls import path

from . import views
urlpatterns = [
    path("show_meal",views.meal, name = 'show_meal'),
]

from django.urls import path

from . import views

urlpatterns = [
    path("about_page", views.aboutPage, name = 'about_page')
    
]

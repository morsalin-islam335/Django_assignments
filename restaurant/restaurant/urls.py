
from django.contrib import admin
from django.urls import path, include


#import  views

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.home, name = 'homepage'),
    path("meal/", include("meal.urls")),
    path('about_us/', include("about_us.urls")),


]

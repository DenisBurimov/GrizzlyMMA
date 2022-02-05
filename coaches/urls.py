from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('article/<slug:post_slug>/', views.post, name='post'),
    path('groups/', views.groups, name='groups'),
    path('coaches/', views.coaches, name='coaches'),
]

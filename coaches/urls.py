from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('article/<slug:post_slug>/', views.post, name='post'),
    path('groups/', views.groups, name='groups'),
]
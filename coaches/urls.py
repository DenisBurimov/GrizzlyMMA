from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('staffops/', views.staff_ops, name='staffops'),
    path('staffregistration/', views.staff_registration, name='staffregistration'),
    path('groupsadd/', views.groups_add, name='groupsadd'),
    path('about/', views.about, name='about'),
    path('article/<slug:post_slug>/', views.post, name='post'),
    path('coaches/', views.coaches, name='coaches'),
    path('groups/', views.groups, name='groups'),
    path('schedule/', views.schedule, name='schedule'),
    path('loginredirect/', views.login_redirect, name='loginredirect'),
    path('staffprofile/', views.staff_profile, name='staffprofile'),
]

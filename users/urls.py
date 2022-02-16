from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('registration/', views.registration, name='registration'),
    path('student_registration/', views.student_registration, name='student_registration'),
    path('parent_registration/', views.parent_registration, name='parent_registration'),
    path('studentsprofile/', views.students_profile, name='students_profile'),
    path('parentsprofile/', views.parents_profile, name='parents_profile'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
]



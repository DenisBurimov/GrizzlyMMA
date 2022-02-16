from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .forms import ManagerProfileForm, ManagerProfileUpdateForm, UserRegistrationForm, UserUpdateForm, GroupsAddingForm

def home(request):
    data = {
        'page_title' : 'Home Page',
        'posts' : Post.objects.all(),
    }

    return render(request, 'coaches/home.html', data)

def about(request):
    data = {
        'page_title' : 'About Page',
    }

    return render(request, 'coaches/about.html', data)

def groups(request):
    data = {
        'page_title' : 'Grizzly MMA Groups',
        'testing_content' : "Groups Page Testing Content",
    }

    return render(request, 'coaches/groups.html', data)

def coaches(request):
    data = {
        'page_title' : 'Тренерская',
        'testing_content' : "Тренерская",
    }

    return render(request, 'coaches/coaches.html', data)

def schedule(request):
    data = {
        'page_title' : 'Расписание',
        'testing_content' : "Расписание",
    }

    return render(request, 'coaches/schedule.html', data)

def staff_registration(request):
    if request.method == "POST":
        r_form = UserRegistrationForm(request.POST)
        p_form = ManagerProfileForm(request.POST, request.FILES)
        if r_form.is_valid() and p_form.is_valid():
            new_user = r_form.save(commit=False)
            new_profile = p_form.save(commit=False)
            new_user.save()
            new_profile.user = new_user
            new_profile.save()

            username = r_form.cleaned_data.get('username')
            messages.success(request, f"Account created for {username}")
            return redirect('login')
    else:
        r_form = UserRegistrationForm()
        p_form = ManagerProfileForm()

    data = {
        'page_title' : 'Registration Page',
        'r_form' : r_form,
        'p_form' : p_form,
    }

    return render(request, 'coaches/staff_registration.html', data)

def staff_profile(request):
    u_form = UserUpdateForm(instance=request.user)
    p_form = ManagerProfileUpdateForm(instance=request.user.manager)
    if request.method == "POST":
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ManagerProfileUpdateForm(request.POST, request.FILES, instance=request.user.manager)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f"Your account has been updated!")
            return redirect('staffprofile')

    data = {
        'page_title': 'Staff Profile Page',
        'u_form': u_form,
        'p_form': p_form,
    }

    return render(request, 'users/profile.html', data)

def login_redirect(request):
    data = {
        'page_title' : 'Testing Page',
    }

    return render(request, 'coaches/login_redirect.html', data)

def post(request, post_slug):
    post = get_object_or_404(Post, slug=post_slug)

    data = {
        'page_title' : 'Home Page',
        'post' : post,
    }

    return render(request, 'coaches/article.html', data)

def staff_ops(request):
    return render(request, 'coaches/staff_ops.html')

def groups_add(request):
    groups_adding_form = GroupsAddingForm()
    if request.method == "POST":
        groups_adding_form = GroupsAddingForm(request.POST)
        if groups_adding_form.is_valid():
            groups_adding_form.save()
            messages.success(request, f"New group has been added!")
            return redirect('groups')

    data = {
        'page_title': 'Group Adding Page',
        'form': groups_adding_form,
    }

    return render(request, 'coaches/groups_add.html', data)

from django.shortcuts import render, redirect
from .forms import UserRegistrationForm, UserProfileForm, UserUpdateForm, ProfileUpdateForm
from django.contrib import messages

def registration(request):
    if request.method == "POST":
        r_form = UserRegistrationForm(request.POST)
        p_form = UserProfileForm(request.POST, request.FILES)
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
        p_form = UserProfileForm()

    data = {
        'page_title' : 'Registration Page',
        'r_form' : r_form,
        'p_form' : p_form,
    }

    return render(request, 'users/registration.html', data)

def profile(request):
    if request.method == "POST":
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(data=request.FILES, instance=request.user.userprofile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f"Your account has been updated!")
            return redirect('profile')
        else:
            messages.error(request, f"Something went wrong")
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.userprofile)

    data = {
        'page_title': 'Profile Page',
        'u_form': u_form,
        'p_form': p_form,
    }

    return render(request, 'users/profile.html', data)

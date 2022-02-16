from django.shortcuts import render, redirect
from .forms import UserRegistrationForm, StudentProfileForm, UserUpdateForm, StudentProfileUpdateForm, \
    ParentProfileForm, ParentProfileUpdateForm, RelationshipForm
from django.contrib import messages


def registration(request):
    data = {
        'page_title': 'Type of Registration',
    }

    return render(request, 'users/registration.html', data)


def student_registration(request):
    if request.method == "POST":
        r_form = UserRegistrationForm(request.POST)
        p_form = StudentProfileForm(request.POST, request.FILES)
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
        p_form = StudentProfileForm()

    data = {
        'page_title': 'Registration Page',
        'r_form': r_form,
        'p_form': p_form,
    }

    return render(request, 'users/student_registration.html', data)


def parent_registration(request):
    if request.method == "POST":
        r_form = UserRegistrationForm(request.POST)
        p_form = ParentProfileForm(request.POST, request.FILES)
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
        p_form = StudentProfileForm()

    data = {
        'page_title': 'Registration Page',
        'r_form': r_form,
        'p_form': p_form,
    }

    return render(request, 'users/parent_registration.html', data)


def students_profile(request):
    u_form = UserUpdateForm(instance=request.user)
    p_form = StudentProfileUpdateForm(instance=request.user.student)
    if request.method == "POST":
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = StudentProfileUpdateForm(request.POST, request.FILES, instance=request.user.student)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f"Your account has been updated!")
            return redirect('students_profile')

    data = {
        'page_title': 'Профиль ученика',
        'u_form': u_form,
        'p_form': p_form,
    }

    return render(request, 'users/profile.html', data)


def parents_profile(request):
    u_form = UserUpdateForm(instance=request.user)
    p_form = StudentProfileUpdateForm(instance=request.user.parent)
    if request.method == "POST":
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ParentProfileUpdateForm(request.POST, request.FILES, instance=request.user.parent)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f"Your account has been updated!")
            return redirect('parents_profile')

    data = {
        'page_title': 'Профиль родителя',
        'u_form': u_form,
        'p_form': p_form,
    }

    return render(request, 'users/profile.html', data)



def relationship(request):
    form = RelationshipForm()
    if request.method == "POST":
        form = RelationshipForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Relationships added")
            return redirect()


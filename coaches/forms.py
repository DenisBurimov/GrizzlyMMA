from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Manager, Group


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    first_name = forms.CharField(required=False)
    last_name = forms.CharField(required=False)
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']


class ManagerProfileForm(forms.ModelForm):
    phone_number = forms.CharField()
    picture = forms.FileField(required=False)

    class Meta:
        model = Manager
        fields = ['phone_number', 'picture']


class ManagerProfileUpdateForm(forms.ModelForm):
    picture = forms.ImageField()
    group = forms.CharField(required=False)

    class Meta:
        model = Manager
        fields = ['phone_number', 'picture']

class GroupsAddingForm(forms.ModelForm):
    group_name = forms.CharField()
    age = forms.CharField()
    coach = forms.ModelChoiceField(queryset=Manager.objects.all())

    class Meta:
        model = Group
        fields = ['group_name', 'age', 'coach']

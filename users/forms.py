from django import forms
from django.contrib.auth.models import User
from .models import Student, Parent, Relationship
from coaches.models import Group
from django.contrib.auth.forms import UserCreationForm

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class StudentProfileForm(forms.ModelForm):
    phone_number = forms.CharField()
    picture = forms.FileField(required=False)

    class Meta:
        model = Student
        fields = ['phone_number', 'picture']

class ParentProfileForm(forms.ModelForm):
    phone_number = forms.CharField()
    picture = forms.FileField(required=False)

    class Meta:
        model = Parent
        fields = ['phone_number', 'picture']

class UserUpdateForm(forms.ModelForm):
    first_name = forms.CharField(required=False)
    last_name = forms.CharField(required=False)
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']

class StudentProfileUpdateForm(forms.ModelForm):
    picture = forms.ImageField()
    group = forms.ModelChoiceField(queryset=Group.objects.all())

    class Meta:
        model = Student
        fields = ['phone_number', 'picture']

class ParentProfileUpdateForm(forms.ModelForm):
    picture = forms.ImageField()

    class Meta:
        model = Parent
        fields = ['phone_number', 'picture']

class RelationshipForm(forms.ModelForm):
    child = forms.CharField()
    parent = forms.CharField()

    class Meta:
        model = Relationship
        fields = ['child', 'parent']

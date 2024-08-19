from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Task, Profile
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    USER_TYPE_CHOICES = [
        ('client', 'Client'),
        ('runner', 'Runner'),
    ]
    user_type = forms.ChoiceField(choices=USER_TYPE_CHOICES, required=True, label="Register as")

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class CustomAuthenticationForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ('username', 'password')

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'phone_number', 'location_from', 'location_to']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'border rounded w-full py-2 px-3', 'placeholder': 'Task Title'}),
            'description': forms.Textarea(attrs={'class': 'border rounded w-full py-2 px-3', 'placeholder': 'Task Description'}),
            'phone_number': forms.TextInput(attrs={'class': 'border rounded w-full py-2 px-3', 'placeholder': 'Contact Phone Number'}),
            'location_from': forms.TextInput(attrs={'class': 'border rounded w-full py-2 px-3', 'placeholder': 'Pickup Location'}),
            'location_to': forms.TextInput(attrs={'class': 'border rounded w-full py-2 px-3', 'placeholder': 'Delivery Location'}),
        }

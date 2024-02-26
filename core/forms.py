from dataclasses import fields
from django import forms 
from django.forms import ModelForm
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UsernameField



class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = '__all__'
        



class CustomUserChangeForm(UserChangeForm):
    '''This form is for user update in django admin'''

    class Meta:
        model = User

        exclude = ('password',)








class signupForm(UserCreationForm):
    password1 = forms.CharField(label = 'Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label = 'Confirm Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    class Meta:
        model  = User
        fields = ['username','first_name','last_name','email']
        labels = {'first_name':'First Name','last_name':'Last Name','email':'Email'}
        widgets = {'username':forms.TextInput(attrs={'class':'form-control'}),'first_name':forms.TextInput(attrs={'class':'form-control'}),
        'last_name':forms.TextInput(attrs={'class':'form-control'}),'email':forms.TextInput(attrs={'class':'form-control'})}
        
class signinForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'autofocus':True,'class':'form-control'}))
    password = forms.CharField(label= 'Password',strip  =False,widget=forms.PasswordInput(attrs = {'class':'form-control','autocomplete':'current-password'}))



class StudentsForm(forms.ModelForm):
    class Meta:
        model = Students
        fields = '__all__'

   
        
        widgets = { 
            'name':forms.TextInput(attrs={'class':"w-full p-2 border rounded-md mb-2"}),
            'package':forms.Select(attrs={'class':'w-full p-2 border rounded-md mb-2'}),
            'course':forms.Select(attrs={'class':'w-full p-2 border rounded-md mb-2'}),
            'payable_fee':forms.TextInput(attrs={'class':"w-full p-2 border rounded-md mb-2",'placeholder':"Enter the field here"}),



        }

        # widgets = { 
        #     'name':forms.PasswordInput
        # }
        # for field_name, field in self.fields.items():
        #     field.widget.attrs.update({
        #         'class': 'w-full p-2 border rounded-md mb-2',
        #     })

        # # Add specific Tailwind CSS classes for certain fields if needed
        # self.fields['payable_fee'].widget.attrs.update({'class': 'w-full p-2 border rounded-md mb-2'})
        # self.fields['collage'].widget.attrs.update({'class': 'w-full p-2 border rounded-md mb-2'})
        # self.fields['time_slot'].widget.attrs.update({'class': 'w-full p-2 border rounded-md mb-2'})
        # self.fields['referred_by'].widget.attrs.update({'class': 'w-full p-2 border rounded-md mb-2'})


class RegisterForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = '__all__'
        

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['title']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline'})
        }

class MentorForm(forms.ModelForm):
    class Meta:
        model = Mentor
        fields = ['user']
        widgets = {
            'user': forms.TextInput(attrs={})
            # Add more widgets for additional fields in the Mentor model
        }



# forms.py
from django import forms
from django.contrib.auth.forms import PasswordChangeForm

class ChangePasswordForm(PasswordChangeForm):
    old_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'mt-1 p-2 w-full border rounded-md focus:outline-none focus:ring focus:border-blue-300'})
    )
    
    new_password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': ' mt-1 block w-full rounded-md transition duration-300 focus:outline-none focus:ring focus:border-blue-300 focus:ring-blue-200 focus:ring-opacity-50'}),
        help_text="Your password must contain at least 8 characters."
    )
    
    new_password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': ' mt-1 block w-full rounded-md transition duration-300 focus:outline-none focus:ring focus:border-blue-300 focus:ring-blue-200 focus:ring-opacity-50'}),
        help_text="Enter the same password as before, for verification."
    )
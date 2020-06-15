from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from.models import Profile



class UserRegisterForm(UserCreationForm):
   # first_name=forms.CharField(max_length=30,required=False,help_text='Enter Your Name ')
   # last_name=forms.CharField(max_length=30,required=False,help_text='Enter Your Surname')
    email=forms.EmailField(help_text='Enter valid email ')
   # phone_number=forms.IntegerField(help_text='Enter valid phone number ')

    class Meta:
        model=User
       # fields=['username','first_name','last_name','email','phone_number','password1','password2']
        fields=['username','email','password1','password2']

    # def save(self, commit=True):
    #     user=super(UserRegisterForm,self).save(commit=True)
    #     user.first_name= self.cleaned_data['first_name']
    #     user.last_name=self.cleaned_data['last_name']
    #     user.phone_number=self.cleaned_data['phone_number']
    #     if commit:
    #         user.save()
    #     return user

class UserUpdateForm(forms.ModelForm):
    first_name=forms.CharField(max_length=30,required=True,help_text='Enter Your Name ')
    last_name=forms.CharField(max_length=30,required=True,help_text='Enter Your Surname')
    email=forms.EmailField(required=True,help_text='Enter email address')


    class Meta:
        model=User
        fields=['username','first_name','last_name','email']


    def save(self, commit=True):
        user=super(UserUpdateForm,self).save(commit=True)
        user.first_name= self.cleaned_data['first_name']
        user.last_name=self.cleaned_data['last_name']

        if commit:
            user.save()
        return user


class ProfileUpdateForm(forms.ModelForm):
    bio=forms.CharField(max_length=200,required=True,help_text='Enter Bio \n For e.g I am interested in blog writing , or special technical blog writing .')
    phone_number=forms.IntegerField(help_text='Enter valid phone number')

    class Meta:
        model=Profile
        fields=['profile_pic','bio','phone_number']

    def save(self, commit=True):
        user=super(ProfileUpdateForm,self).save(commit=True)
        user.phone_number=self.cleaned_data['phone_number']
        user.bio=self.cleaned_data['bio']
        if commit:
            user.save()
        return user



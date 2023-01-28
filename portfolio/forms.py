from .validators import validate_email
from paypal.pro.fields import CreditCardField, CreditCardExpiryField, CreditCardCVV2Field, CountryField
from django import forms
from .models import *

class ContactForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    subject = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    message = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    
class ReviewForm(forms.ModelForm):
    class Meta:
        model = Course_Reviews
        fields = ('user_name','comment','rating')

class StudentRegisterForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput())
    email = forms.EmailField(validators = [validate_email])
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = Students
        fields = [
            'username',
            'full_name',
            'email',
            'password',
            'address'
        ]
    def clean_username(self):
        user_name = self.cleaned_data["username"]
        if User.objects.filter(username=user_name).exists():
            raise forms.ValidationError("Student with this username already exists.")
        return user_name
    
class StudentLoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput())
    
    def clean_username(self):
        user_name = self.cleaned_data.get("username")

        if User.objects.filter(username=user_name).exists():
           pass
        else:
            raise forms.ValidationError('Student with this username is not exists.')
        return user_name

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Students
        fields = ['full_name','address','image','phone']

class PasswordForm(forms.Form):
    email = forms.CharField(widget=forms.EmailInput(attrs={
        "class":"form-control",
        "placeholder":"Enter Your Email here..."
    })) 
    
    def clean_email(self):
        e = self.cleaned_data.get("email")
        if Students.objects.filter(user__email=e).exists():
            pass
        else:
            raise forms.ValidationError("Student with this account does not exists ....")
        return e
        
class PasswordResetForm(forms.Form):
    new_password = forms.CharField(widget=forms.PasswordInput(attrs={
        "class":"form-control",
        "autocomplete" : "new-password",
        "placeholder":"Enter your new password here.."
    }),label = "New Password")
    
    confirm_new_password = forms.CharField(widget=forms.PasswordInput(attrs={
        "class":"form-control",
        "autocomplete" : "new-password",
        "placeholder":"Confirm your new password here.."
    }),label = "Confirm New Password")
    
    def clean_confirm_new_password(self):
        new_password = self.cleaned_data.get('new_password')
        confirm_new_password = self.cleaned_data.get('confirm_new_password')
        if new_password != confirm_new_password:
            raise forms.ValidationError('New passwords did not match !')
        return confirm_new_password

class CheckOutForm(forms.ModelForm):
    class Meta:
        model = CourseOrder
        fields = [
            'first_name',
            'last_name',
            'phone_num',
            'email',
        ]

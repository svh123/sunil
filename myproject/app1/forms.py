

from django import forms
from django.core.validators import RegexValidator

class user_reg(forms.Form):

    full_name = forms.CharField(label="Full Name",max_length=100)
    email = forms.EmailField(label="E-Mail",max_length=100)
    passwd = forms.CharField(label="Password",min_length=8,max_length=16,widget=forms.PasswordInput,validators=[RegexValidator('^(\w+\d+|\d+\w+)+$', message="Password should be a combination of Alphabets and Numbers")])
    passwd1 = forms.CharField(label="Password", min_length=8, max_length=16, widget=forms.PasswordInput)
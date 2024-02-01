from django import forms
from django.core.exceptions import ValidationError
from django.forms import ModelForm
from .models import Author,Post




class PostForm(forms.Form):
    name = forms.CharField(max_length=36)
    descrition=forms.CharField(max_length=300)
    is_active = forms.BooleanField()

    def save(self):
        name = self.cleaned_data["name"]
        description = str(self.cleaned_data["description"])
        is_active = self.cleaned_data["is_active"]
        post = Post.objects.create(name=name, description=description, is_active=is_active)
        return post



class UserRegisterModelForm(forms.ModelForm):
    password1 = forms.CharField(max_length=128)
    password2 = forms.CharField(max_length=128)

    def save(self, commit=True):
        password1 = self.cleaned_data["password1"]
        password2 = self.cleaned_data["password2"]
        if password1==password2:
            user = super().save(commit)
            user.set_password(password1)
            user.save()
        else:
            raise ValidationError("Password must be match")

    class Meta:
        model = Author
        fields = ["username",  "email", "first_name", "last_name", "password1", "password2"]


class UserLoginForm(forms.Form):
    username = forms.CharField(max_length=128)
    password = forms.CharField(max_length=128)
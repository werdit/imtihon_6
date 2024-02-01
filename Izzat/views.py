from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.template import loader
from django.http import HttpResponse
from django.views import View

from Izzat.forms import UserLoginForm, UserRegisterModelForm


def home_page(request):
    template=loader.get_template('blog/home.html')
    return HttpResponse(template.render())
def about_page(request):
    template = loader.get_template('blog/about.html')
    return HttpResponse(template.render())

def post_confirm_delete_page(request):
    template = loader.get_template('blog/post_confirm_delete.html')
    return HttpResponse(template.render())
def post_detail_page(request):
    template = loader.get_template('blog/post_detail.html')
    return HttpResponse(template.render())
def post_form_page(request):
    template = loader.get_template('blog/post_form.html')
    return HttpResponse(template.render())
def user_post_page(request):
    template = loader.get_template('blog/user_posts.html')
    return HttpResponse(template.render())

class UserRegisterView(View):
    def get(self, request):
        form = UserRegisterModelForm()
        return render(request, "bookshop/register.html", {"form": form})

    def post(self, request):
        form = UserRegisterModelForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("bookshop:login")
        else:
            return render(request, "bookshop/register.html", {"form": form})


class UserLoginView(View):
    def get(self, request):
        form = UserLoginForm()
        return render(request, "bookshop/login.html", {"form": form})

    def post(self, request):
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                print(request.COOKIES)
                return redirect("bookshop:home-page")
            else:
                return redirect("bookshop:login")

        else:
            return render(request, "bookshop/login.html", {"form": form})


def postcreate(request):
    form = SpecialityForm
    if request.method == "POST":
        form = SpecialityForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('courses:home-page')
        else:
            return render(request, "courses/speciality_create.html", context={"form": form})


    else:
        return render(request, "courses/speciality_create.html", context={"form": form})

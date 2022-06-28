from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages

# Create your views here.
from main.forms import NewUserForm, UserProfileForm, ContactForm


def homepage(request):
   messages.add_message(request, messages.INFO, 'Hello world.')
   return render(
       request,
       template_name="base.html",
       context={}
   )

def register_request(request):
    if request.method == "POST":
        form = NewUserForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.add_message(request, messages.SUCCESS, "User registered.")
            messages.add_message(request, messages.INFO, "User logged in.")
            return redirect("/")

    form = NewUserForm()
    return render(
        request=request,
        template_name="main/register.html",
        context={'register_form': form}
    )

def login_request(request):

    if request.method == "POST":
        #pobieramy dane z formularza
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")

            #spradzamy czy dane pasują do użytkownika
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}")
                return redirect("/")
            else:
                messages.error(request, "Invalid username or password")
        else:
            messages.error(request, "Invalid username or password")

    form = AuthenticationForm()
    return render(
        request=request,
        template_name="main/login.html",
        context={"login_form":form},
    )

def logout_request(request):
    logout(request)
    messages.info(request, "You are successfully logged out")
    return redirect("/")

def user_profile(request, id):
    user = User.objects.get(pk=id)
    try:
        profile = user.userprofile
    except AttributeError:
        profile = None
    except Exception:
        profile = None


    if request.method == "POST":
        form = UserProfileForm(data=request.POST, instance=profile)
        if form.is_valid():
                profile.save()

    if profile:
        form = UserProfileForm(instance=profile)
    else:
        form = UserProfileForm()


    return render(
        request,
        "main/userprofile.html",
        context={'form':form,
                 'userprofile': profile}
    )

def content(request):
    form = ContactForm()
    if request.method == "POST":
        form = ContactForm(data=request.POST)
    if form.is_valid():
        data = form.cleaned_data
        print("wysyłka maila...", data)

        return render(
            request,
            'main/userprofile.html',
            context=


        )
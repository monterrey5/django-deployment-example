from django.shortcuts import render
from basic_app.forms import UserForm, UserProfileInfoForm


# From Login lecture
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
#for view that requires user to be logged in
from django.contrib.auth.decorators import login_required



# Create your views here.

def index(request):
    return render(request, "basic_app/index.html")


# From Login lecture - if login is login_required

@login_required
def special(request):
    return HttpResponse("you are logged in. nice.")

# the decorator is used to require user to be logged in
@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))



def register(request):

    registered = False

    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():

            user = user_form.save()
            # hashing the password
            user.set_password(user.password)
            user.save()

# commit=FALSE (line below) to edit profile before saving it to database
            profile = profile_form.save(commit=False)
            profile.user = user
# ABOVE:
# not commiting to database yet, so it does not colide with user above
# the last line (profile.user = user) sets up one to one relationship


# this request.FILES (line below) will be used in case CSV, PDF etc. files will be uploaded
            if "profile_pic" in request.FILES:
                profile.profile_pic = request.FILES["profile_pic"]

            profile.save()
            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    return render(request, "basic_app/registration.html",
                            {"user_form": user_form,
                            "profile_form": profile_form,
                            "registered": registered})

#From Login Lecture
#func names should not have names we import
def user_login(request):

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        # there should be username=username, pass..= pass.., not just (username, password)
        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Account Not Active.")
        else:
            print("Some tried to log in and failed.")
            print("Username {}, Password {}".format(username, password))
            return HttpResponse("Invalid login details supplied.")
    else:
        return render(request, "basic_app/login.html", {})

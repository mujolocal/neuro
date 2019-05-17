from django.shortcuts import render
from .forms import LoginForm
from django.contrib.auth import authenticate, login, logout
# Create your views here.
def auth(request):
    current_user = request.user.id
    
    print("this is the current user",current_user)
    user = None
    if request.method == "POST":
        print("this is request type", request.POST.get("username"))
        user = authenticate(username = request.POST.get("username"),
            password =request.POST.get("password"))
        if user != None:
            login(request,user)
            print("{} Logged in".format(user))
        else:
            logout(request)
            print("invalid user")
    
    return render(request, "authentication/login.html",{"form": LoginForm()})
    
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


# Create your views here.



def signup(request):
    if request.method == 'POST':
        name = request.POST['name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['cpassword']

        if password != confirm_password:
            return render(request, 'accounts/signup.html')
        messages.error(request, "Password do not match !!")

        user = User.objects.create_user(username, email, password)
        user.save()

        return redirect('accounts:signin')
    else:
        return render(request, 'accounts/signup.html')


def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "signed in success!!")
            return redirect('store:index')
        else:
            messages.error(request, "Password do not match !!")
            return render(request, 'acounts/signin.html')
    else:
        return render(request, 'accounts/signin.html')




def logout_user(request):
    logout(request)
    messages.success(request, "logged out!!")
    return redirect('accounts:signin')

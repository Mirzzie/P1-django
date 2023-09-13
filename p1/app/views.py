from django.shortcuts import render


# Create your views here.

def index(request):
    return render(request, 'index.html')

def signup(request):
    if request.method == 'POST':
        Name = request.post['Name']
        Username = request.post['username']
        Email = request.post['Email']
        Password = request.post['Password']
        Confirm_password = request.post['cpassword']
    else:
        return render(request, 'signup.html')

def signin(request):
     if request.method == 'POST':
        Username = request.post['username']
        Password = request.post['Password']
     else:
      return render(request, 'signin.html')

def cart(request):
    return render(request, 'cart.html')
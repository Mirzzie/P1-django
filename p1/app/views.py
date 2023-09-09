from django.shortcuts import render


# Create your views here.

def index(request):
    return render(request, 'index.html')

def register(request):
    if request.method == 'POST':
        Name = request.post['Name']
        Email = request.post['Email']
        Password = request.post['Password']
        Address = request.post['Address']
    else:
        return render(request, 'register.html')
        
def login(request):
        return render(request, 'login.html')
 
def cart(request):
    return render(request, 'cart.html')
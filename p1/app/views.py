from django.shortcuts import render


# Create your views here.

def index(request):
    return render(request, 'index.html')
def register(request):
    if request.method == 'POST':
        Firstname = request.post['Firstname']
        Lastname = request.post['Lastname']
        Email = request.post['Email']
        Password = request.post['Password']
        Address = request.post['Address']
        City = request.post['City']
        State = request.post['State']
    return render(request, 'register.html')

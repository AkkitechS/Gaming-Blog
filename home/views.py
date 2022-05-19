from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import Contact
from blog.models import BlogModel

# Create your views here.


def home(request):
    return render(request, 'home/index.html')


def about(request):
    return render(request, 'home/about.html')


def contact(request):
    if request.method == 'POST':
        print(request.POST)
        fName = request.POST['firstName']
        lName = request.POST['lastName']
        email = request.POST['rEmail']
        phone = request.POST['phone']
        query = request.POST['query']

        contactModel = Contact(firstName=fName, lastName=lName, email=email, phNo=phone, query=query)
        contactModel.save()
        messages.success(request, 'Query sent successfully')
    return render(request, 'home/contact.html')


def blog(request):
    blog = BlogModel.objects.all()
    return render(request, 'home/blogs.html', {'blog':blog})


def search(request):
    query = request.GET['query']
    post = BlogModel.objects.filter(title__icontains=query)
    print(post)
    return render(request, 'home/search.html', {'post':post, 'query':query})


def signup(request):
    if request.method == 'POST':
        fName = request.POST['fName']
        lName = request.POST['lName']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        cPassword = request.POST['cpassword']

        myUser = User.objects.create_user(username, email, password)
        myUser.first_name = fName
        myUser.last_name = lName
        myUser.save()
        return redirect('/')
    return render(request, 'home/signup.html')


def userLogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/')
    return render(request, 'home/login.html')


def userLogout(request):
    logout(request)
    return redirect('/')
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib import messages
from django.contrib.auth.models import User, auth
from .models import blog_post, book_list, author, profile_info
from django.views.generic.list import ListView
from twilio.rest import Client
from django.conf import settings  



def home_page(request):
    message_to_broadcast = ("Someone visisted Your website just now")
    client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
    for recipient in settings.SMS_BROADCAST_TO_NUMBERS:
        if recipient:
            client.messages.create(to=recipient,from_=settings.TWILIO_NUMBER,body=message_to_broadcast)
    if request.user.is_authenticated:
        return redirect("/blog")
    else:
        return render(request, "home.html")


def sign_up(request):
	return render(request, "sign_up.html")

def book(request):
    if request.user.is_authenticated:
        authors = author.objects.all()
        books = book_list.objects.all()
        if 'search' in request.GET:
            query = request.GET["search"]
            post = book_list.objects.filter(book_name__contains=query)
            print(post)
            return render( request,'search.html',{'post':post})
        else:
            return render(request, "book_list.html",{'authors':authors,'books':books})

    else:
        return redirect('/')

def blog(request):
    if request.user.is_authenticated:
        blog_posts= blog_post.objects.all()
        return render(request,"blog.html", {'posts':blog_posts})
    else:
        return redirect('/')

def login(request):
    if request.method=='POST':
        username = request.POST["username"]
        password = request.POST["password"]

        user = auth.authenticate(username = username, password=password)
        if user is not None:
            auth.login(request,user)

            return redirect("/blog")
        else:
            messages.info(request, "Access Denied")
            return redirect("/")
    else:
        return redirect("/")

def logout(request):
    auth.logout(request)
    return redirect ('/')

def joinus(request):
    first_name = request.POST["first_name"]
    last_name = request.POST["last_name"]
    username = request.POST["username"]
    email = request.POST["email"]
    pass1= request.POST["password1"]
    pass2 = request.POST["password2"]

    if len(pass1) < 6:
        messages.info(request,"Password Should be 6-10 character")
        return redirect ('/sign_up')

    if pass1!=pass2:
        messages.info(request,"Passwords didn't match")
        return redirect ('/sign_up')
    if User.objects.filter(username=username).exists():
        messages.info(request,"username taken")
        return redirect ('/sign_up')
    if User.objects.filter(email=email).exists():
        messages.info(request,"already have an account on this email")
        return redirect ('/sign_up')
    else:
        user= User.objects.create_user(first_name=first_name, last_name = last_name, username=username, email=email,password=pass1)
        user.save()
        auth.login(request,user)
        return redirect("/blog")

def add_post(request):
    if request.user.is_authenticated:
        title = request.POST['title']
        detail = request.POST['detail']
        posts = blog_post(title= title, detail=detail, user_id=request.user.id, user_name=request.user.username)
        posts.save()
        return redirect("/blog")
    else:
        return redirect('/')

def edit(request, pk):
    e_post = blog_post.objects.get(id=pk)
    if request.user.id == e_post.user_id:
        return render(request, "edit_page.html",{"e_post":e_post})
    else:
        return redirect("/blog")

def editing(request):
    id = request.POST['id']
    title = request.POST['title']
    post = request.POST['detail']
    e_post = blog_post.objects.get(id=id)
    e_post.title = title
    e_post.detail = post
    e_post.save()
    return redirect("/blog")


def delete_post(request, pk):
    blog_post.objects.order_by('detail')
    e_post = blog_post.objects.get(id=pk)
    if request.user.id == e_post.user_id:
        e_post.delete()
        return redirect("/blog")
    else:
        return redirect("/blog")

def all_writers(request):
    if request.user.is_authenticated:
        writers = author.objects.all()
        return render (request, 'all_writers.html',{'writers':writers})
    else:
        return redirect('/')

def profile(request):
    if request.user.is_authenticated:
        info = User.objects.filter(id=request.user.id)
        for a in info:
            print(a.id)
        return render(request,'profile.html',{'info':info})
    else:
        return redirect('/')

def contact(request):
    return render(request, "contact.html")

def author_book_list(request,pk):
    author_books = book_list.objects.filter(Author_name__id=pk)
    return render(request, "author_book_list.html",{"author_books":author_books})

def borrow(request, pk):
    return render (request, "borrow.html")


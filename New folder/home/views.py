from multiprocessing import context
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.core.paginator import Paginator
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from . models import CompanyProfile, Phone, Type
from . forms import ContactForm
from userprofile.models import Customer
from userprofile.forms import SignupForm

# Create your views here.
def home (request):
    cprofile = CompanyProfile.objects.get(pk=1)
    featured = Phone.objects.filter(feature=True)
    bestselling = Phone.objects.filter(best_selling=True)
    latest = Phone.objects.filter(latest=True)
    category = Type.objects.all()

    context = {
        'featured':featured,
        'bestselling':bestselling,
        'latest':latest,
    }
    
    return render(request, 'index.html', context)

def products(request):
    cprofile = CompanyProfile.objects.get(pk=1)
    product = Phone.objects.all()
    p = Paginator(product, 8)
    page = request.GET.get('page')
    paginate = p.get_page(page)

    context = {
        'paginate':paginate,
    }

    return render(request, 'products.html',context)

def category(request, id):
    brand = Type.objects.get(pk=id)
    phonecat = Phone.objects.filter(type_id = id)



    context = {
        'brand':brand,
        'phonecat':phonecat
    }    

    return render(request, 'category.html', context)

def detail(request, id, slug):
    phonedet = Phone.objects.get(pk=id)

    context = {
        'phonedet':phonedet
    }    

    return render(request, 'detail.html', context)


def about(request):
    aboutus = CompanyProfile.objects.get(pk=1)

    context = {
        'aboutus':aboutus
    }   

    return render(request, 'about.html', context)

def contact(request):
    contact = ContactForm()
    if request.method == 'POST':
        contact = ContactForm(request.POST)
        if contact.is_valid():
            contact.save()
            messages.success(request,'your message has been sent successfully, one of our representative will get back to you shortly')
            return redirect('home')

    context = {
        'contact': contact
    }

    return render(request,'contact.html', context)

def signout(request):
    logout(request)
    messages.success(request, 'you are now signed out')
    return redirect('home')


def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            messages.success(request, 'login successful!!')
            return redirect('home')
        else:
            messages.info(request, 'username/password is incorrect')

    return render(request, 'signin.html')   

def signup (request):
    form = SignupForm()
    if request.method == 'POST':
        phone = request.POST['phone']
        address = request.POST['address']
        pix = request.POST['pix']
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            newuser = Customer(user=user)
            newuser.username = user.username 
            newuser.first_name = user.first_name 
            newuser.last_name = user.last_name 
            newuser.email = user.email 
            newuser.phone = phone 
            newuser.address = address 
            newuser.pix = pix 
            newuser.save()
            messages.success(request, f'congratulations {user.username} your registration is successful')
            return redirect('signin')
        else:
            messages.error(request, form.errors)

    return render(request, 'signup.html')  

#user profile
def profile(request):
    userprof = Customer.objects.get(user__username = request.user.username)

    context = {
        'userprof':userprof
    }

    return render(request, 'profile.html', context) 

def profile_update(request):
    userprof = Customer.objects.get(user__username = request.user.username)
    form = CustomerForm(instance=request.user.customer)
    if request.method == 'POST':
        form = CustomerForm(request.POST, request.FILES, instance=request.user.customer)
        if form.is_valid():
            user = form.save()
            new = user.first_name.title()
            messages.success(request, f'Dear{new}, your profile has been updated successfully')
            return redirect(profile)
        else:
            new = user.first_name.title()
            messages.error(request, f'Dear {new}, your profile update generated the following errors: {form.errors}')
            return redirect('profile_update')

    context = {
        'userprof':userprof
    }

    return render(request, 'profile_update.html',context)        
           

#user profile done

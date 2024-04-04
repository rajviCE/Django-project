from pyexpat.errors import messages
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django import forms
from django.forms.formsets import formset_factory
from datetime import datetime
from .models import package
from .models import pessanger_detail
from .forms import ContactForm
# Create your views here.

def index(request):
    return render(request,'index.html')




def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                return HttpResponse("Username is already taken")
            elif User.objects.filter(email=email).exists():
                return HttpResponse("Email is already registered")
            else:
                user = User.objects.create_user(username=username, password=password1, email=email, last_name=last_name,
                                                first_name=first_name)
                user.save()
                print('User created')
                # login(request, user)  # Corrected login function
                return redirect('login')
        else:
            print("Passwords do not match")
            return redirect('register')
       
    else:
        return render(request, 'register.html')

    
def login(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return render(request, 'index.html')
        else:
           return HttpResponse("username or password are incorrect")
       
    return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect('login')

def about(request):
    return render(request,'about.html')

def destination_details(request,city_name):
    dest = package.objects.get(package_name=city_name)
    price = dest.package_price
    request.session['price'] = price
    request.session['city'] = city_name
    return render(request,'destination_details.html',{'dest':dest})
    
@login_required(login_url='login')
def destination_list(request,city_name):
    dests = package.objects.all().filter(country=city_name)
    return render(request,'travel_destination.html',{'dests': dests})

def search(request):
    try:
        place1 = request.GET['place']
        # print(place1)
        dest = package.objects.get(package_name=place1)
        # print(place1)
        return render(request, 'destination_details.html', {'dest': dest})
    except:
        # messages.info(request, 'Place not found')
        return redirect('index')
    
class KeyValueForm(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()
    age = forms.IntegerField()
def pessanger_detail_def(request):
    KeyValueFormSet = formset_factory(KeyValueForm, extra=1)
    if request.method == 'POST':
        formset = KeyValueFormSet(request.POST)
        if formset.is_valid():
            # Fetch package price per person
            package = package.objects.get(id=request.session['package_id'])
            price_per_person = package.price

            # Calculate total price based on the number of passengers
            num_passengers = formset.total_form_count()
            total_price = num_passengers * price_per_person

            # Save passenger details to database
            trip_date = datetime.strptime(request.POST['trip_date'], "%Y-%m-%d").date()
            username = request.user.get_username()
            city = request.session['city']
            for form in formset:
                pessanger_detail.objects.create(
                    Trip_same_id=request.session['Trip_same_id'],
                    first_name=form.cleaned_data['first_name'],
                    last_name=form.cleaned_data['last_name'],
                    age=form.cleaned_data['age'],
                    Trip_date=trip_date,
                    payment=price_per_person,
                    username=username,
                    city=city
                )

            # Update Trip_same_id in session
            request.session['Trip_same_id'] += num_passengers

            # Calculate total bill
            GST = total_price * 0.18
            GST = round(GST, 2)
            final_total = total_price + GST

            # Store total bill in session
            request.session['total_price'] = final_total

            # Redirect to confirmation page
            return redirect('confirmation')
    else:
        formset = KeyValueFormSet()

    return render(request, 'sample.html', {'formset': formset})


def confirmation(request):
    total_price = request.session.get('total_price', 0)
    return render(request, 'confirmation.html', {'total_price': total_price})

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('thank_you')  # Redirect to a thank you page after successful submission
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})


def thank_you(request):
    return render(request, 'thank_you.html')

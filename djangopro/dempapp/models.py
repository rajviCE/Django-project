from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class user(models.Model):
    user_id = models.IntegerField(primary_key=True)
    email = models.CharField(max_length = 20)
    password = models.CharField(max_length = 10)
    name = models.CharField(max_length=20)
    age = models.IntegerField(max_length = 3)
    gender = models.CharField(max_length=1)
    contact_no = models.IntegerField(max_length=10)
    address = models.CharField(max_length=25)

class accomodation(models.Model):
    acc_id = models.IntegerField(primary_key=True)
    hotel_name = models.CharField(max_length=15)
    address = models.CharField(max_length=20)
    hotel_cno = models.IntegerField()
    hotel_price_per_night = models.IntegerField()

class transportation(models.Model):
    transport_id = models.IntegerField(primary_key=True)
    transportation_type = models.CharField(max_length=10)
    pick_date = models.DateField()
    drop_date = models.DateField()
    pick_address = models.CharField(max_length=25)
    drop_address = models.CharField(max_length=25)
    transport_price = models.IntegerField()

class package(models.Model):
    package_id = models.IntegerField(primary_key=True)
    package_name = models.CharField(max_length=15)
    photo = models.ImageField(upload_to='static/images',default="")
    p_transport_id = models.ForeignKey(transportation,null = True,on_delete = models.CASCADE)
    P_acc_id = models.ForeignKey(accomodation,null = True,on_delete = models.CASCADE)
    package_description = models.CharField(max_length=100)
    days = models.IntegerField()
    package_price = models.IntegerField()
    day1=models.TextField()
    day2=models.TextField()
    day3=models.TextField()
    day4=models.TextField()
    day5=models.TextField()
    day6=models.TextField()

class booking(models.Model):
    book_id = models.IntegerField(primary_key=True)
    book_user_id = models.ForeignKey(user,null = True,on_delete = models.CASCADE)
    book_package_id = models.ForeignKey(package,null = True,on_delete = models.CASCADE)
    book_start_date = models.DateField()
    book_end_date = models.DateField()
    number_of_person = models.IntegerField()

class payment(models.Model):
    pay_id = models.IntegerField(primary_key=True)
    p_book_id = models.ForeignKey(booking,null = True,on_delete = models.CASCADE)
    p_user_id = models.ForeignKey(user,null = True,on_delete = models.CASCADE)
    total_payment = models.IntegerField()
    payment_type = models.CharField(max_length=10)

class reviews_and_ratings(models.Model):
    r_user_id = models.ForeignKey(user,null = True,on_delete = models.CASCADE)
    review = models.CharField(max_length = 100)

class pessanger_detail(models.Model):
    Trip_id = models.AutoField(primary_key=True)
    Trip_same_id = models.IntegerField(default=1)
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    age = models.IntegerField(default=10)
    username = models.CharField(max_length=10)
    Trip_date = models.DateField()
    payment = models.IntegerField(default=50)
    city = models.CharField(max_length=20)
    pay_done = models.IntegerField(default=0)
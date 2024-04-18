from django.contrib.auth.models import User
from django.db import models


class Musician(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    instrument = models.CharField(max_length=100)

    def str(self):
        return f"{self.first_name} {self.last_name}"


class Album(models.Model):
    artist = models.ForeignKey(Musician, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    release_date = models.DateField()
    num_stars = models.IntegerField()

    def str(self):
        return self.name


class Person(models.Model):
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30, default='Doe')
    mail = models.EmailField(max_length=100)
    birthday = models.DateField()
    password = models.CharField(max_length=257, default='default_password')
    phone = models.CharField(max_length=12, default='000-000-0000')

    def __str__(self):
        return f"{self.name} {self.surname}"


class School(models.Model):
    school_address = models.CharField(max_length=255)
    school_number = models.CharField(max_length=255)


class Class(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    class_location = models.CharField(max_length=255)


class PersonalInfo(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    address = models.CharField(max_length=255)
    class_number = models.CharField(max_length=255, null=True, blank=True)



class Stuff(models.Model):
    stuff_name = models.CharField(max_length=30)
    stuff_desc = models.CharField(max_length=257)
    photo = models.CharField(max_length=100)
    price = models.IntegerField()


class Basket(models.Model):
    Basket_id = models.IntegerField()
    stuff_id = models.IntegerField()
    person_id = models.IntegerField()
    date = models.DateField()


class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, through='OrderItem')
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def __str__(self):
        return f"{self.quantity} - {self.product.name}"

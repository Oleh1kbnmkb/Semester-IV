from django.contrib.auth.models import User
from django.db import models
import uuid
from django.db import models


class AdvUser(models.Model):
  is_activated = models.BooleanField(default=True)
  user = models.OneToOneField(User, on_delete=models.CASCADE)


class Spare(models.Model):
  name = models.CharField(max_length=30)


class Machine(models.Model):
  name = models.CharField(max_length=30)
  spares = models.ManyToManyField(Spare)


class Musician(models.Model):
  FIRST_NAME = {
    "A": "Alexander",
    "B": "Rimma",
    "C": "Oleg",
    "D": "Timofey"
  }

  first_name = models.CharField(max_length=1, choices=FIRST_NAME)
  last_name = models.CharField(max_length=50)
  instrument = models.CharField(max_length=100)

  def str(self):
    return f"{self.first_name} {self.last_name}"


class Album(models.Model):
  NUM_STARS = {
    "1": "⭐",
    "2": "⭐⭐",
    "3": "⭐⭐⭐",
    "4": "⭐⭐⭐⭐",
    "5": "⭐⭐⭐⭐⭐"
  }
  artist = models.ForeignKey(Musician, on_delete=models.CASCADE)
  name = models.CharField(max_length=100)
  release_date = models.DateField()
  num_stars = models.IntegerField(choices=NUM_STARS)


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
  FIRST_NAME = {
    "A": "Alexander",
    "B": "Rimma",
    "C": "Oleg",
    "D": "Timofey"
  }

  first_name = models.CharField(max_length=1, choices=FIRST_NAME)
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


class Student(models.Model):
  name = models.CharField(max_length=100)
  surname = models.CharField(max_length=100)
  student_card_number = models.CharField(max_length=20)
  email = models.EmailField()

  def __str__(self):
    return f"{self.name} {self.surname}"


class StudentGroup(models.Model):
  group_number = models.CharField(max_length=10)
  password = models.CharField(max_length=50)
  meeting_room = models.CharField(max_length=50)

  def __str__(self):
    return self.group_number


class LibraryCard(models.Model):
  student = models.OneToOneField(Student, on_delete=models.CASCADE)
  issue_date = models.DateField()
  expiration_date = models.DateField()
  price = models.DecimalField(max_digits=10, decimal_places=2)

  def __str__(self):
    return f"Library Card for {self.student}"


class LibraryLiterature(models.Model):
  title = models.CharField(max_length=200)
  genre = models.CharField(max_length=100)
  publication_date = models.DateField()
  year = models.PositiveIntegerField()

  def __str__(self):
    return self.title


class BookBorrowingProcess(models.Model):
  library_card = models.ForeignKey(LibraryCard, on_delete=models.CASCADE)
  literature = models.ForeignKey(LibraryLiterature, on_delete=models.CASCADE)
  borrowing_date = models.DateField()
  giver_name = models.CharField(max_length=200)

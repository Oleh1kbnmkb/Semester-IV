from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models



class Rubric(models.Model):
  name = models.CharField(max_length=100)

  def __str__(self):
    return self.name


class Bb(models.Model):
  title = models.CharField(max_length=100)
  content = models.TextField()
  price = models.DecimalField(max_digits=10, decimal_places=2)
  rubric = models.ForeignKey(Rubric, on_delete=models.CASCADE)

  def __str__(self):
    return self.title


class GoITeens(models.Model):
  title = models.CharField(max_length=100)
  content = models.TextField(null=True, blank=True)
  price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
  rubric = models.ForeignKey(Rubric, on_delete=models.CASCADE, null=True, blank=True)

  def title_and_price(self):
    if self.price:
      return '%s (%.2f)' % (self.title, self.price)
    else:
      return self.title

  def __str__(self):
    return self.title


class Spare(models.Model):
  name = models.CharField(max_length=30)

  def __str__(self):
    return self.name


class Machine(models.Model):
  name = models.CharField(max_length=30)
  spares = models.ManyToManyField(Spare)

  def __str__(self):
    return self.name


class AdvUser(models.Model):
  is_activated = models.BooleanField(default=True)
  user = models.OneToOneField(User, on_delete=models.CASCADE)

  def __str__(self):
    return self.user.username


class Musician(models.Model):
  first_name = models.CharField(max_length=50)
  last_name = models.CharField(max_length=50)
  instrument = models.CharField(max_length=100)

  def __str__(self):
    return f"{self.first_name} {self.last_name}"


class Album(models.Model):
  artist = models.ForeignKey(Musician, on_delete=models.CASCADE)
  name = models.CharField(max_length=100)
  release_date = models.DateField()
  num_stars = models.IntegerField()

  def __str__(self):
    return self.name


class School(models.Model):
  school_address = models.CharField(max_length=255)
  school_number = models.CharField(max_length=255)


class Class(models.Model):
  school = models.ForeignKey(School, on_delete=models.CASCADE)
  class_location = models.CharField(max_length=255)


class PersonalInfo(models.Model):
  FIRST_NAME_CHOICES = [
    ("A", "Alexander"),
    ("B", "Rimma"),
    ("C", "Oleg"),
    ("D", "Timofey"),
    ("E", "Kostya"),
  ]

  first_name = models.CharField(max_length=1, choices=FIRST_NAME_CHOICES)
  last_name = models.CharField(max_length=255)
  school = models.ForeignKey(School, on_delete=models.CASCADE)
  address = models.CharField(max_length=255)
  class_number = models.CharField(max_length=255, null=True, blank=True)


class Stuff(models.Model):
  stuff_id = models.IntegerField()
  stuff_name = models.CharField(max_length=30)
  stuff_desc = models.CharField(max_length=257)
  photo = models.CharField(max_length=100)
  price = models.FloatField()
  rate = models.IntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(10)])

  def publish(self):
    self.save()



class Category(models.Model):
  name = models.CharField(max_length=100)
  description = models.TextField()

  def __str__(self):
    return self.name


class Product(models.Model):
  person_id = models.IntegerField()
  name = models.CharField(max_length=100)
  description = models.TextField()
  price = models.DecimalField(max_digits=10, decimal_places=2)
  new = models.BooleanField(default=False)
  rating = models.DecimalField(max_digits=3, decimal_places=2, default=0)

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


# Нові моделі
class Author(models.Model):
  first_name = models.CharField(max_length=50)
  last_name = models.CharField(max_length=50)

  def __str__(self):
    return f"{self.first_name} {self.last_name}"


class AuthorProfile(models.Model):
  author = models.OneToOneField(Author, on_delete=models.CASCADE)
  biography = models.TextField()


class Book(models.Model):
  title = models.CharField(max_length=100)
  author = models.ForeignKey(Author, on_delete=models.CASCADE)
  published_date = models.DateField()

  def __str__(self):
    return self.title


class Library(models.Model):
  name = models.CharField(max_length=100)
  books = models.ManyToManyField(Book)

  def __str__(self):
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


class NewArrivals(models.Model):
  arrivals_name = models.CharField(max_length=255)
  arrivals_desc = models.CharField(max_length=350)
  arrivals_price = models.CharField(max_length=255)
  photo = models.CharField(max_length=100)

  def __str__(self):
    return self.arrivals_name

class Comment(models.Model):
  product = models.ForeignKey(NewArrivals, related_name='comments', on_delete=models.CASCADE)
  author = models.CharField(max_length=100)
  text = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return f'Comment by {self.author} on {self.product}'


class Basket(models.Model):
  person = models.ForeignKey(Person, on_delete=models.CASCADE, null=True, blank=True)
  session_key = models.CharField(max_length=40, null=True, blank=True)
  product = models.ForeignKey(NewArrivals, on_delete=models.CASCADE)
  count = models.PositiveIntegerField(default=1)

  def __str__(self):
    return f"{self.product.arrivals_name} - {self.count}"


class FeaturedProduct(models.Model):
  product = models.ForeignKey('Product', on_delete=models.CASCADE)
  def __str__(self):
    return self.product.name


class TopProduct(models.Model):
  product = models.ForeignKey('Product', on_delete=models.CASCADE)
  def __str__(self):
    return self.product.name

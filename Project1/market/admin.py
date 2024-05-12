from django.contrib import admin
from .models import Musician, Album, Person, School, Class, PersonalInfo, Stuff, Category, Product, UserProfile, Order, OrderItem, Student, StudentGroup, LibraryCard, LibraryLiterature, BookBorrowingProcess, AdvUser, Spare, Machine


@admin.register(Musician, Album, Person, School, Class, PersonalInfo,
                Stuff, Category, Product, UserProfile, Order, OrderItem, Student,
                StudentGroup, LibraryCard, LibraryLiterature, BookBorrowingProcess,
                AdvUser, Spare, Machine)

class MyModelAdmin(admin.ModelAdmin):
  list_per_page = 20
  list_select_related = True

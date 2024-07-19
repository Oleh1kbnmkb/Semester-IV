from django.contrib import admin
from .models import (Musician, Album, Person,
                     PersonalInfo, School, Class,
                     Stuff, GoITeens, AdvUser,
                     Category, Product, UserProfile,
                     Order, OrderItem, Bb, Spare, Machine,
                     Author, AuthorProfile, Book, Library,
                     NewArrivals, FeaturedProduct,
                     TopProduct, Basket)


@admin.register(Musician, Album, Person,
                PersonalInfo, School, Class,
                Stuff, GoITeens, AdvUser,
                Category, Product, UserProfile,
                Order, OrderItem, Bb, Spare, Machine,
                Author, AuthorProfile, Book, Library,
                NewArrivals, FeaturedProduct,
                TopProduct, Basket)
class MyModelAdmin(admin.ModelAdmin):
    list_per_page = 20
    list_select_related = True

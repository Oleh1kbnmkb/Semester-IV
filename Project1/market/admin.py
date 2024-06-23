from django.contrib import admin
from .models import (Musician, Album, Person,
                     PersonalInfo, School, Class,
                     Stuff, Basket, GoITeens, AdvUser,
                     Category, Product, UserProfile,
                     Order, OrderItem, Bb, Spare, Machine,
                     Author, AuthorProfile, Book, Library,
                     NewArrivals, BestSellers, FeaturedProduct,
                     TopProduct)


@admin.register(Musician, Album, Person,
                PersonalInfo, School, Class,
                Stuff, Basket, GoITeens, AdvUser,
                Category, Product, UserProfile,
                Order, OrderItem, Bb, Spare, Machine,
                Author, AuthorProfile, Book, Library,
                NewArrivals, BestSellers, FeaturedProduct,
                TopProduct)
class MyModelAdmin(admin.ModelAdmin):
    list_per_page = 20
    list_select_related = True

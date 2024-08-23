from django.contrib import admin
from .models import (LastNews)


@admin.register(LastNews)
class MyModelAdmin(admin.ModelAdmin):
  list_per_page = 20
  list_select_related = True

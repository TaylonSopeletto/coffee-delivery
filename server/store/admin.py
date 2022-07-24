from django.contrib import admin
from .models import Coffee, Category
# Register your models here.


@admin.register(Coffee)
class CoffeeAdmin(admin.ModelAdmin):
    pass

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass
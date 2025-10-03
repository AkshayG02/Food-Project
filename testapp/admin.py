from django.contrib import admin
from .models import Food

# Register your models here.
class FoodAdmin(admin.ModelAdmin):
    list_display=["id","name", "price", "category", "img"]
admin.site.register(Food, FoodAdmin)
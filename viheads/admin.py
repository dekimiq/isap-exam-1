from django.contrib import admin
from .models import Idea, Difficulty, CartItem, Cart

admin.site.register(Idea)
admin.site.register(Difficulty)

# Register your models here.

class CartItemInline(admin.TabularInline):
  model = CartItem
  extra = 1

class CartAdmin(admin.ModelAdmin):
  inlines = [CartItemInline]

admin.site.register(Cart, CartAdmin)

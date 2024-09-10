from django.contrib import admin
from .models import Restaurant, Category, Item

@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    list_display = ('name', 'location')
    search_fields = ('name', 'location')
    list_filter = ('location',)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'restaurant')
    search_fields = ('name', 'restaurant__name')
    list_filter = ('restaurant',)

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'restaurant', 'category')
    search_fields = ('name', 'restaurant__name', 'category__name')
    list_filter = ('restaurant', 'category')



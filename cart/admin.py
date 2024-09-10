from django.contrib import admin
from .models import CartItem, Cart

@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ('item', 'quantity', 'total_price')
    search_fields = ('item__name',)

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('id', 'total_items_price', 'grand_total')
    filter_horizontal = ('items',)

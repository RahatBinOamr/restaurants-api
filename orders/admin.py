from django.contrib import admin
from .models import Order, OrderContactInfo

class OrderInline(admin.TabularInline):
    model = Order
    extra = 1  # Number of empty forms to display in the admin

class ContactAdmin(admin.ModelAdmin):
    inlines = [OrderInline]

admin.site.register(OrderContactInfo, ContactAdmin)
admin.site.register(Order)

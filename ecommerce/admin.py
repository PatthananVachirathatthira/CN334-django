from django.contrib import admin
from ecommerce.models import (
    Customer, Product, Shipping, Payment, Order, ProductOrder
)

# Register your models here.
@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'user__first_name', 'user__last_name', 'province', 'post_code', 'tel', 'email', 'created_at')
    search_fields = ('user__username', 'user__first_name', 'user__last_name', 'province', 'post_code', 'tel', 'email', 'created_at')
    list_filter = ('province',)
    ordering = ('id',)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'stock', 'category')
    search_fields = ('name', 'category')
    ordering = ('id',)

@admin.register(Shipping)
class ShippingAdmin(admin.ModelAdmin):
    list_display = ('id', 'method', 'fee')
    list_filter = ('method',)
    search_fields = ('id',)

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('id', 'payment_owner', 'method', 'card_no', 'expired', 'holder_name')
    search_fields = ('payment_owner__username', 'method', 'card_no', 'holder_name')
    list_filter = ('method',)
    ordering = ('id',)

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer', 'total_price', 'status', 'shipping', 'payment')
    search_fields = ('status', 'customer__admin')
    list_filter = ('status',)
    ordering = ('id',)


@admin.register(ProductOrder)
class ProductOrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'order', 'quantity', 'total_price')
    search_fields = ('product__name', 'order__id')
    ordering = ('id',)


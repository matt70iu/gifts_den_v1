from django.contrib import admin
from .models import Product, Category, Review, Wishlist

# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'Category',
        'price',
        'image',
    )

    ordering = ('sku',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        'product',
        'name',
        'body',
    )
    
class WishlistAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'product',
        'added_on',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Wishlist, WishlistAdmin)

from django.contrib import admin
from .models import Product, Category, Review

class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'friendly_name',
        'category',
        'price',
        'rating',
        'image',
    )

    ordering = ('name',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        'product_name',
        'stars',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Review, ReviewAdmin)

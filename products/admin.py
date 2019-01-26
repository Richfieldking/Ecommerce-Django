from django.contrib import admin

from .models import Product

class ProductAdmin(admin.ModelAdmin):
    
        search_fields = ['title', 'description']
        list_display=[ '__unicode__','title', 'price','active', 'updated']
        list_editable = ['price', 'active']
        class Meta:
            model = Product

admin.site.register(Product, ProductAdmin)

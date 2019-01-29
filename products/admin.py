from django.contrib import admin

from .models import Product

class ProductAdmin(admin.ModelAdmin):

        date_hierachy = 'timestamp'
        search_fields = ['title', 'description']
        list_display=[ '__unicode__','title', 'price','active', 'updated']
        list_editable = ['price', 'active']
        readonly_fields =['updated','timestamp']
        prepopulated_fields ={'slug':('title',)}
        class Meta:
            model = Product

admin.site.register(Product, ProductAdmin)

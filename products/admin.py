from django.contrib import admin
from .models import Product,Category,ProductFeature
# Register your models here.

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(ProductFeature)
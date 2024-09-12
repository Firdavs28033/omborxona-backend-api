from django.contrib import admin
from .models import Product, Material, ProductMaterial, Warehouse

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'code')

class MaterialAdmin(admin.ModelAdmin):
    list_display = ('name',)

class ProductMaterialAdmin(admin.ModelAdmin):
    list_display = ('product', 'material', 'quantity')

class WarehouseAdmin(admin.ModelAdmin):
    list_display = ('material', 'remainder', 'price')

admin.site.register(Product, ProductAdmin)
admin.site.register(Material, MaterialAdmin)
admin.site.register(ProductMaterial, ProductMaterialAdmin)
admin.site.register(Warehouse, WarehouseAdmin)

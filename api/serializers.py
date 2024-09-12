from rest_framework import serializers
from .models import Product, Material, ProductMaterial, Warehouse

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'code']

class MaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Material
        fields = ['id', 'name']

class ProductMaterialSerializer(serializers.ModelSerializer):
    product = ProductSerializer()
    material = MaterialSerializer()

    class Meta:
        model = ProductMaterial
        fields = ['product', 'material', 'quantity']

class WarehouseSerializer(serializers.ModelSerializer):
    material = MaterialSerializer()

    class Meta:
        model = Warehouse
        fields = ['material', 'remainder', 'price']

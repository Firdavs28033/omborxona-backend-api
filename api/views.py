from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Product, ProductMaterial, Warehouse
from .serializers import ProductSerializer, ProductMaterialSerializer, WarehouseSerializer

class MaterialRequestView(APIView):
    def post(self, request):
        product_code = request.data.get('product_code')
        quantity = request.data.get('quantity')

        try:
            product = Product.objects.get(code=product_code)
        except Product.DoesNotExist:
            return Response({'error': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)

        materials_needed = ProductMaterial.objects.filter(product=product)
        material_usage = {}
        response_data = []

        for material in materials_needed:
            needed_quantity = material.quantity * quantity
            warehouses = Warehouse.objects.filter(material=material.material).order_by('id')
            total_collected = 0
            used_warehouses = []

            for warehouse in warehouses:
                if total_collected >= needed_quantity:
                    break
                if warehouse.remainder > 0:
                    collected = min(needed_quantity - total_collected, warehouse.remainder)
                    total_collected += collected
                    used_warehouses.append({
                        'warehouse_id': warehouse.id,
                        'material_name': warehouse.material.name,
                        'qty': collected,
                        'price': warehouse.price
                    })

            if total_collected < needed_quantity:
                used_warehouses.append({
                    'warehouse_id': None,
                    'material_name': material.material.name,
                    'qty': needed_quantity - total_collected,
                    'price': None
                })

            response_data.append({
                'product_name': product.name,
                'product_qty': quantity,
                'product_materials': used_warehouses
            })

        return Response({'result': response_data}, status=status.HTTP_200_OK)

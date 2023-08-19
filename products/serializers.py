from rest_framework import serializers
# electronics || Apple || iPhone 12
from products.models import ProductCategory ,Maker, Product

class ProductCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = "__all__"
        depth=1  # this is to populate the foreign key fields by depth one i.e. only the immediate foreign key fields will be populated.


class MakerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Maker
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model= Product
        fields="__all__"
        depth=1

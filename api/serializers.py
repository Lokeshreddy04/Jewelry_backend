from rest_framework import serializers
from .models import Product, Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    # Show category details when reading
    category = CategorySerializer(read_only=True)
    
    # Use category_id when creating
    category_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Product
        fields = '__all__'

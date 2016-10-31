from rest_framework import serializers

from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    """
    Base serializer for a Product
    """
    class Meta:
        model = Product
        fields = ('name', 'is_complete', 'image', 'quantity')

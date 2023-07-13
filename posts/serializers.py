from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.Serializer):
    image = serializers.ImageField(max_length=None, use_url=True)
    title = serializers.CharField(max_length=255)
    description = serializers.CharField(style={'base_template': 'textarea.html'})
    
    def create(self, validated_data):
        return Product.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.image = validated_data.get('image', instance.image)
        instance.save()
        return instance

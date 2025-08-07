from rest_framework import serializers
from .models import products , Cart
from django.contrib.auth.models import User


class UserSignupSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email'),
            password=validated_data['password']
        )
        return user


class productsSerializer(serializers.ModelSerializer):
    class Meta:
        model = products
        fields = '__all__'  # or list specific fields like ['id', 'name', 'email']


# class ProductSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = products
#         fields = '__all__'
class CartSerializer(serializers.ModelSerializer):
    product = productsSerializer()

    class Meta:
        model = Cart
        fields = ['id', 'product', 'quantity', 'created_at']
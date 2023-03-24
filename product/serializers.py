from rest_framework import serializers
from .models import Category, Product, Review


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = 'id stars text product_title'.split()


class ReviewTextSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['text']


class ProductSerializer(serializers.ModelSerializer):
    # rating = ReviewSerializer(many=True)

    class Meta:
        model = Product
        fields = 'id title description price category_name rating'.split()


class CategorySerializer(serializers.ModelSerializer):
    # products_count = ProductSerializer(many=True)
    # products_list = ProductSerializer(many=True)

    class Meta:
        model = Category
        fields = 'id name products_count products_list'.split()


class RatingSerializer(serializers.ModelSerializer):
    reviews = ReviewTextSerializer(many=True)

    class Meta:
        model = Product
        fields = 'title rating reviews'.split()

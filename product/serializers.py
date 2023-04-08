from rest_framework import serializers
from .models import Category, Product, Review, Tag
from rest_framework.exceptions import ValidationError


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = 'id stars text product_title'.split()


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = 'id title description price category_name rating tags_list'.split()


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = 'id name products_count products_list'.split()


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = 'title rating reviews_list'.split()


class ProductValidateSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=100)
    description = serializers.CharField()
    price = serializers.FloatField()
    category_id = serializers.IntegerField()
    tags = serializers.ListField(child=serializers.IntegerField())

    def validate_category_id(self, category_id):
        try:
            Category.objects.get(id=category_id)
        except Category.DoesNotExist:
            raise ValidationError("Category not found!")
        return category_id

    def validate_tags(self, tags):
        all_tags = Tag.objects.filter(id__in=tags)  # Все теги которые есть
        all_objects = Tag.objects.all()  # Все обьекты в тегах
        ids = [id_['id'] for id_ in all_objects.values()]  # все айдишки тегов

        if len(tags) == all_tags.count():  # проверка на совпадение тегов
            return tags

        # вывод индекса тегов которых нет
        raise ValidationError(f'tags {[tags.index(i) for i in tags if i not in ids]} not found!')


class CategoryValidateSerializer(serializers.Serializer):
    name = serializers.CharField()


class ReviewValidateSerialiazer(serializers.Serializer):
    text = serializers.CharField()
    stars = serializers.IntegerField()
    product_id = serializers.IntegerField()

    def validate_product_id(self, product_id):
        try:
            Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            raise ValidationError("Product not found!")
        return product_id

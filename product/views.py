from .serializers import CategorySerializer, ProductSerializer, ReviewSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Category, Product, Review
from rest_framework import status


@api_view(['GET'])
def category_list_api_view(request):
    category_list = Category.objects.all()
    serializer = CategorySerializer(category_list, many=True)
    return Response(data=serializer.data)


@api_view(['GET'])
def category_api_view(request, id_):
    try:
        category = Category.objects.get(id=id_)
    except Category.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND,
                        data={'error': 'Category not found!'})
    serializer = CategorySerializer(category)
    return Response(data=serializer.data)


@api_view(['GET'])
def product_list_api_view(request):
    product_list = Product.objects.all()
    serializer = ProductSerializer(product_list, many=True)
    return Response(data=serializer.data)


@api_view(['GET'])
def product_api_view(request, id_):
    try:
        product = Product.objects.get(id=id_)
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND,
                        data={'error': 'Product not found!'})
    serializer = ProductSerializer(product)
    return Response(data=serializer.data)


@api_view(['GET'])
def review_list_api_view(request):
    review_list = Review.objects.all()
    serializer = ReviewSerializer(review_list, many=True)
    return Response(data=serializer.data)


@api_view(['GET'])
def review_api_view(request, id_):
    try:
        review = Review.objects.get(id=id_)
    except Review.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND,
                        data={'error': 'Review not found!'})
    serializer = ReviewSerializer(review)
    return Response(data=serializer.data)

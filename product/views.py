from .serializers import CategorySerializer, ProductSerializer, ReviewSerializer, RatingSerializer, \
    ProductValidateSerializer, CategoryValidateSerializer, ReviewValidateSerialiazer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Category, Product, Review
from rest_framework import status


@api_view(['GET'])
def products_reviews_rating_view(request):
    products = Product.objects.all()
    serializer = RatingSerializer(products, many=True)
    return Response(data=serializer.data)


@api_view(['GET', 'POST'])
def category_list_api_view(request):
    category_list = Category.objects.all()

    if request.method == "GET":
        serializer = CategorySerializer(category_list, many=True)
        return Response(data=serializer.data)

    elif request.method == "POST":
        serializer = CategoryValidateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        name = serializer.validated_data.get('name')
        category = Category.objects.create(name=name)
        return Response(data=CategorySerializer(category).data)


@api_view(['GET', 'PUT', 'DELETE'])
def category_api_view(request, id_):
    try:
        category = Category.objects.get(id=id_)
    except Category.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND,
                        data={'error': 'Category not found!'})

    if request.method == "GET":
        serializer = CategorySerializer(category)
        return Response(data=serializer.data)

    elif request.method == "PUT":
        serializer = CategoryValidateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        category.name = serializer.validated_data.get('name')
        return Response(data=CategorySerializer(category).data)

    elif request.method == "DELETE":
        category.delete()
        return Response(status=status.HTTP_404_NOT_FOUND, data={'error': 'categories not found!'})


@api_view(['GET', 'POST'])
def product_list_api_view(request):
    if request.method == "GET":
        product_list = Product.objects.all()
        serializer = ProductSerializer(product_list, many=True)
        return Response(data=serializer.data)

    elif request.method == 'POST':
        serializer = ProductValidateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        title = serializer.validated_data.get('title')
        description = serializer.validated_data.get('description')
        price = serializer.validated_data.get('price')
        category_id = serializer.validated_data.get('category_id')
        tags = serializer.validated_data.get('tags')

        products = Product.objects.create(title=title, description=description,
                                          price=price, category_id=category_id)
        products.tags.set(tags)
        products.save()
        return Response(data=ProductSerializer(products).data)


@api_view(['GET', 'PUT', 'DELETE'])
def product_api_view(request, id_):
    try:
        product = Product.objects.get(id=id_)
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND,
                        data={'error': 'Product not found!'})

    if request.method == 'GET':
        serializer = ProductSerializer(product)
        return Response(data=serializer.data)

    elif request.method == 'PUT':
        serializer = ProductValidateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        product.title = serializer.validated_data.get('title')
        product.description = serializer.validated_data.get('description')
        product.price = serializer.validated_data.get('price')
        product.category_id = serializer.validated_data.get('category_id')
        product.tags = serializer.validated_data.get('tags')
        return Response(data=ProductSerializer(product).data)

    elif request.method == 'DELETE':
        product.delete()
        return Response(status=status.HTTP_404_NOT_FOUND,
                        data={'error': 'product not found!'})


@api_view(['GET', 'POST'])
def review_list_api_view(request):
    if request.method == "GET":
        review_list = Review.objects.all()
        serializer = ReviewSerializer(review_list, many=True)
        return Response(data=serializer.data)

    elif request.method == 'POST':
        serializer = ReviewValidateSerialiazer(data=request.data)
        serializer.is_valid(raise_exception=True)
        text = serializer.validated_data.get('text')
        product_id = serializer.validated_data.get('product_id')
        stars = serializer.validated_data.get('stars')
        reviews = Review.objects.create(text=text, stars=stars, product_id=product_id)
        return Response(data=ReviewSerializer(reviews).data)


@api_view(['GET', 'PUT', 'DELETE'])
def review_api_view(request, id_):
    try:
        review = Review.objects.get(id=id_)
    except Review.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND,
                        data={'error': 'Review not found!'})
    if request.method == 'GET':
        serializer = ReviewSerializer(review)
        return Response(data=serializer.data)

    elif request.method == 'PUT':
        serializer = ReviewValidateSerialiazer(data=request.data)
        serializer.is_valid(raise_exception=True)
        review.text = serializer.validated_data.get('text')
        review.product_id = serializer.validated_data.get('product_id')
        review.stars = serializer.validated_data.get('stars')
        return Response(data=ReviewSerializer(review).data)

    elif request.method == 'DELETE':
        review.delete()
        return Response(status=status.HTTP_404_NOT_FOUND,
                        data={'error': 'review not found!'})

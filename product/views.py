from .serializers import CategorySerializer, ProductSerializer, ReviewSerializer, RatingSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Category, Product, Review
from rest_framework import status


@api_view(['GET'])
def product_list_api_view(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(data=serializer.data)


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
        name = request.data.get('name')
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
        category.name = request.data.get('name')
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
        title = request.data.get('title')
        description = request.data.get('description')
        price = request.data.get('price')
        category_id = request.data.get('category_id')

        products = Product.objects.create(title=title, description=description,
                                          price=price, category_id=category_id)
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
        product.title = request.data.get('title')
        product.description = request.data.get('description')
        product.price = request.data.get('price')
        product.category_id = request.data.get('category_id')
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
        text = request.data.get('text')
        product_id = request.data.get('product_id')
        stars = request.data.get('stars')
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
        review.text = request.data.get('text')
        review.product_id = request.data.get('product_id')
        review.stars = request.data.get('stars')
        return Response(data=ReviewSerializer(review).data)

    elif request.method == 'DELETE':
        review.delete()
        return Response(status=status.HTTP_404_NOT_FOUND,
                        data={'error': 'review not found!'})

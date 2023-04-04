from .serializers import CategorySerializer, ProductSerializer, ReviewSerializer, RatingSerializer, \
    ProductValidateSerializer, CategoryValidateSerializer, ReviewValidateSerialiazer
from rest_framework.response import Response
from .models import Category, Product, Review
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework import status


class CategoryAPIView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    pagination_class = PageNumberPagination

    def post(self, request, *args, **kwargs):
        serializer = CategoryValidateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        name = serializer.validated_data.get('name')
        category = Category.objects.create(name=name)
        return Response(data=CategorySerializer(category).data)


class CategoryDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    pagination_class = PageNumberPagination
    lookup_url_kwarg = 'id_'
    lookup_field = 'id'

    def put(self, request, *args, **kwargs):
        serializer = CategoryValidateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        category = Category.objects.all()
        category.name = serializer.validated_data.get('name')
        return Response(data=CategorySerializer(category).data)


class ProductReviewRatingAPIView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = RatingSerializer
    pagination_class = PageNumberPagination


class ProductAPIView(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = PageNumberPagination
    validate_serializer_class = ProductValidateSerializer

    def post(self, request, *args, **kwargs):
        serializer = ProductValidateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        title = serializer.validated_data.get('title')
        description = serializer.validated_data.get('description')
        price = serializer.validated_data.get('price')
        category_id = serializer.validated_data.get('category_id')
        tags = serializer.validated_data.get('tags')
        product = Product.objects.create(title=title, description=description,
                                         price=price, category_id=category_id)
        product.tags.set(tags)
        product.save()
        serializer = self.get_serializer(product)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class ProductDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = PageNumberPagination
    lookup_url_kwarg = 'id_'
    lookup_field = 'id'

    def put(self, request, *args, **kwargs):
        serializer = ProductValidateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        product = Product.objects.all()
        product.title = serializer.validated_data.get('title')
        product.description = serializer.validated_data.get('description')
        product.price = serializer.validated_data.get('price')
        product.category_id = serializer.validated_data.get('category_id')
        product.tags = serializer.validated_data.get('tags')
        return Response(data=ProductSerializer(product).data)


class ReviewAPIView(ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    pagination_class = PageNumberPagination

    def post(self, request, *args, **kwargs):
        serializer = ReviewValidateSerialiazer(data=request.data)
        serializer.is_valid(raise_exception=True)
        text = serializer.validated_data.get('text')
        product_id = serializer.validated_data.get('product_id')
        stars = serializer.validated_data.get('stars')
        reviews = Review.objects.create(text=text, stars=stars, product_id=product_id)
        return Response(data=ReviewSerializer(reviews).data)


class ReviewDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    pagination_class = PageNumberPagination
    lookup_field = 'id'
    lookup_url_kwarg = 'id_'

    def put(self, request, *args, **kwargs):
        serializer = ReviewValidateSerialiazer(data=request.data)
        serializer.is_valid(raise_exception=True)
        review = Review.objects.all()

        review.text = serializer.validated_data.get('text')
        review.product_id = serializer.validated_data.get('product_id')
        review.stars = serializer.validated_data.get('stars')
        return Response(data=ReviewSerializer(review).data)

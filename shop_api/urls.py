from django.contrib import admin
from django.urls import path, include
from product import views


urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/v1/categories/', views.CategoryAPIView.as_view()),
    path('api/v1/categories/<int:id_>/', views.CategoryDetailAPIView.as_view()),

    path('api/v1/products/', views.ProductAPIView.as_view()),
    path('api/v1/products/<int:id_>/', views.ProductDetailAPIView.as_view()),
    path('api/v1/products/reviews/', views.ProductReviewRatingAPIView.as_view()),

    path('api/v1/reviews/', views.ReviewAPIView.as_view()),
    path('api/v1/reviews/<int:id_>/', views.ReviewDetailAPIView.as_view()),

    path('api/v1/users/', include('users.urls'))
]

from django.contrib import admin
from django.urls import path, include
from product import views


urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/v1/categories/', views.category_list_api_view),
    path('api/v1/categories/<int:id_>/', views.category_api_view),

    path('api/v1/products/', views.product_list_api_view),
    path('api/v1/products/<int:id_>/', views.product_api_view),
    path('api/v1/products/reviews/', views.products_reviews_rating_view),

    path('api/v1/reviews/', views.review_list_api_view),
    path('api/v1/reviews/<int:id_>/', views.review_api_view),

    path('api/v1/users/', include('users.urls'))
]

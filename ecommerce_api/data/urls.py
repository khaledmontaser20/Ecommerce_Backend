from .views import *
from django.urls import path
from . import views


urlpatterns = [
    path('products/<str:pk>/', ProductDetail.as_view()),
    path('products/', ProductList.as_view()),
    path('categories/<str:pk>/', CategoryDetail.as_view()),
    path('categories/', CategoryList.as_view()),
    path('reviews/<str:pk>/', ReviewDetail.as_view()),
    path('reviews/', ReviewList.as_view()),
]

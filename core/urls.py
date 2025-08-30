from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet
from .views import BlogPostViewSet, ProductViewSet, CategoryViewSet, TagViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'blogs', BlogPostViewSet, basename="blog")
router.register(r'products', ProductViewSet, basename="product")
router.register(r'categories', CategoryViewSet, basename="category")
router.register(r'tags', TagViewSet, basename="tag")

urlpatterns = [
    path("api/", include(router.urls)),
]

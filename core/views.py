from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from django.core.exceptions import ValidationError
from .models import BlogPost, Product, Category, Tag
from django.contrib.auth.models import User
from rest_framework import viewsets
from .serializers import UserSerializer
from .serializers import BlogPostSerializer, ProductSerializer, CategorySerializer, TagSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    
class BlogPostViewSet(viewsets.ModelViewSet):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', 'content']
    ordering_fields = ['published_date']
    ordering = ['-published_date']

    def get_queryset(self):
        queryset = super().get_queryset()
        start_date = self.request.query_params.get("start_date")
        end_date = self.request.query_params.get("end_date")

        try:
            if start_date and end_date:
                queryset = queryset.filter(published_date__range=[start_date, end_date])
            elif start_date:
                queryset = queryset.filter(published_date__gte=start_date)
            elif end_date:
                queryset = queryset.filter(published_date__lte=end_date)
        except Exception:
            raise ValidationError({"error": "Invalid date format. Use YYYY-MM-DD."})

        return queryset


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ["category", "available"]
    search_fields = ["title", "description"]

    def get_queryset(self):
        queryset = super().get_queryset()
        min_price = self.request.query_params.get("minPrice")
        max_price = self.request.query_params.get("maxPrice")

        try:
            if min_price:
                queryset = queryset.filter(price__gte=min_price)
            if max_price:
                queryset = queryset.filter(price__lte=max_price)
        except ValueError:
            raise ValidationError({"error": "Invalid price format. Must be a number."})

        return queryset


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

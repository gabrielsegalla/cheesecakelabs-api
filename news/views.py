from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import permission_classes
from news.models import News, Category, Author
from rest_framework.response import Response
from news.serializers import NewsSerializer, CategoriesSerializer, AuthorSerializer


class NewsViewSet(viewsets.ModelViewSet):
    pagination_class = None
    queryset = News.objects.all()
    serializer_class = NewsSerializer


class CategoriesViewSet(viewsets.ModelViewSet):
    pagination_class = None
    queryset = Category.objects.all()
    serializer_class = CategoriesSerializer


class AuthorViewSet(viewsets.ModelViewSet):
    pagination_class = None
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
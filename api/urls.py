from django.urls import path, include
from rest_framework import routers
from news.views import NewsViewSet, CategoriesViewSet, AuthorViewSet

router = routers.DefaultRouter()
router.register(r"news", NewsViewSet)
router.register(r"categories", CategoriesViewSet)
router.register(r"author", AuthorViewSet)

urlpatterns = [
    path("", include(router.urls)),
]

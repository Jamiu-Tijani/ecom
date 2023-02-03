from django.urls import path, include
from rest_framework.routers import DefaultRouter


from .viewsets import ProductViewSet
# from . import  views
router = DefaultRouter()
router.register(r"product", ProductViewSet, basename="product")

urlpatterns = [
    path("", include(router.urls)),
    # path("category/", views.CategoryListAPIView.as_view()),
    # path("product/category/<int:pk>/", views.CategoryAPIView.as_view()),
    # path("product/list/", views.ListProductAPIView.as_view()),
    # path("product/serpylist/", views.SerpyListProductAPIView.as_view()),
    # path("product/list-user-product/", views.ListBusinessProductAPIView.as_view()),
    # path("product/create/product/", views.CreateProductAPIView.as_view()),
    # path("product/product/<int:pk>/delete/", views.DestroyProductAPIView.as_view()),
    # path("product/product/<str:uuid>/", views.ProductDetailView.as_view()),
    # path("product/views/", views.ProductViewsAPIView.as_view()),
    ]
from django.urls import path, include
from rest_framework.routers import DefaultRouter


from .viewsets import BusinessViewSet

router = DefaultRouter()
router.register(r"business", BusinessViewSet, basename="business")

urlpatterns = [
    path("", include(router.urls)),]
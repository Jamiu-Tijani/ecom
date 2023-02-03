from django.db import transaction
from rest_framework import viewsets, serializers
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated,AllowAny
from .serializers import ProductFeatureSerializer
from accounts.serializers import inline_serializer
from .services import ProductService
from accounts.mixins import CustomResponseMixin
from django.core.validators import MinValueValidator

class ProductViewSet(CustomResponseMixin, viewsets.ViewSet):
    @action(detail=False, methods=["post"], url_path="create", permission_classes=[IsAuthenticated])
    @transaction.atomic
    def create_product(self, request):
        serialized_data = inline_serializer(
            fields={
                "shop_name" : serializers.CharField(max_length=255),
                "title" : serializers.CharField(max_length=1000),
                "price" : serializers.FloatField(validators=[MinValueValidator(0.0)]),
                "image" : serializers.ImageField(required=False),
                "description" : serializers.CharField(max_length=255),
                "quantity" : serializers.IntegerField(validators=[MinValueValidator(0)]),
                "category" : serializers.CharField(max_length=200),
                "category_parent" : serializers.CharField(max_length=200,required=False),
                "features" : ProductFeatureSerializer(many=True,required=True),
                #"feature_values" : ProductFeatureSerializer(many=True,required=True),
            },
            data=request.data)

        errors = self.validate_serializer(serialized_data)
        #serialize_feature = ProductFeaturesSerializer(data={"features":[dict(x) for x in serialized_data.validated_data.get("features")]})
        #print([dict(x) for x in serialized_data.validated_data.get("features")])
        #print(serialize_feature.is_valid(raise_exception=True))
        if errors:
            return errors

        response = ProductService().create_product(request=request, **serialized_data.validated_data)
        return self.response(response)

    @action(detail=False, methods=["get"], url_path="retrieve-business-products", permission_classes=[AllowAny])
    @transaction.atomic
    def retrieve_business_products(self, request):
        serialized_data = inline_serializer(
            fields={
                "shop_name" : serializers.CharField(max_length=255),
            },
            data=request.data)
        errors = self.validate_serializer(serialized_data)

        if errors:
            return errors

        response = ProductService().retrieve_business_products(request=request, **serialized_data.validated_data)
        return self.response(response)

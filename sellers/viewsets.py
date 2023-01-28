from django.db import transaction
from rest_framework import viewsets, serializers
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated,AllowAny
from .choices import *
from accounts.serializers import inline_serializer
from .services import BussinessService
from accounts.mixins import CustomResponseMixin

class BusinessViewSet(CustomResponseMixin, viewsets.ViewSet):
    @action(detail=False, methods=["post"], url_path="create", permission_classes=[IsAuthenticated])
    @transaction.atomic
    def create_business(self, request):
        serialized_data = inline_serializer(
            fields={
    "seller_id" : serializers.UUIDField(auto_created=True),
    "shop_name" : serializers.CharField(max_length=255),
    "contact_address" : serializers.CharField(max_length=1000),
    "postal_code" : serializers.CharField(max_length=10),
    "business_type" : serializers.CharField(choices=BUSINESS_TYPE,max_length=20),
    "full_name" : serializers.CharField(max_length=255),
    "phone_number" : serializers.CharField(max_length=20),
    "extra_phone_number" : serializers.CharField(max_length=20),
    "legal_id" : serializers.ImageField(),
    "referrer" : serializers.EmailField(max_length=50),
    "no_of_employees" :serializers.CharField(choices=EMPLOYEES,),
    "business_reg_number" : serializers.CharField(max_length=255,null=True),
    "registeration_certificate" : serializers.ImageField(),
    "legal_entity_country" : serializers.CharField(max_length=255),
    "shipping_country" : serializers.CharField(max_length=255)
            },
            data=request.data)
        errors = self.validate_serializer(serialized_data)
        if errors:
            return errors


        response = BussinessService().create_business(request=request, **serialized_data.validated_data)

        return self.response(response)

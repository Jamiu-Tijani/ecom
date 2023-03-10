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
    "shop_name" : serializers.CharField(max_length=255),
    "contact_address" : serializers.CharField(max_length=1000),
    "postal_code" : serializers.CharField(max_length=10),
    "business_type" : serializers.ChoiceField(choices=BUSINESS_TYPE),
    "full_name" : serializers.CharField(max_length=255),
    "phone_number" : serializers.CharField(max_length=20),
    "extra_phone_number" : serializers.CharField(max_length=20, required=False),
    "legal_id" : serializers.ImageField(required=False),
    "referrer" : serializers.EmailField(max_length=50, required=False),
    "no_of_employees" :serializers.ChoiceField(choices=EMPLOYEES,),
    "business_reg_number" : serializers.CharField(max_length=255,required=False),
    "registeration_certificate" : serializers.ImageField(required=False),
    "legal_entity_country" : serializers.CharField(max_length=255,required=False),
    "shipping_country" : serializers.CharField(max_length=255)
            },
            data=request.data)
        errors = self.validate_serializer(serialized_data)
        if errors:
            return errors


        response = BussinessService().create_business(request=request, **serialized_data.validated_data)

        return self.response(response)
    @action(detail=False, methods=["post"], url_path="update", permission_classes=[IsAuthenticated])
    @transaction.atomic
    def update_business(self, request):
        serialized_data = inline_serializer(
            fields={
    "shop_name" : serializers.CharField(max_length=255),
    "contact_address" : serializers.CharField(max_length=1000,required=False),
    "postal_code" : serializers.CharField(max_length=10,required=False),
    "business_type" : serializers.ChoiceField(choices=BUSINESS_TYPE,required=False),
    "full_name" : serializers.CharField(max_length=255,required=False),
    "phone_number" : serializers.CharField(max_length=20,required=False),
    "extra_phone_number" : serializers.CharField(max_length=20, required=False),
    "legal_id" : serializers.ImageField(required=False),
    "referrer" : serializers.EmailField(max_length=50,required=False),
    "no_of_employees" :serializers.ChoiceField(choices=EMPLOYEES,required=False),
    "business_reg_number" : serializers.CharField(max_length=255,required=False),
    "registeration_certificate" : serializers.ImageField(required=False),
    "legal_entity_country" : serializers.CharField(max_length=255,required=False),
    "shipping_country" : serializers.CharField(max_length=255,required=False)
            },
            data=request.data)
        errors = self.validate_serializer(serialized_data)
        if errors:
            return errors


        response = BussinessService().update_business(request=request, **serialized_data.validated_data)

        return self.response(response)
    
    @action(detail=False, methods=["post"], url_path="delete", permission_classes=[IsAuthenticated])
    @transaction.atomic
    def delete_business(self, request):
        serialized_data = inline_serializer(
            fields={
    "shop_name" : serializers.CharField(max_length=255),
            },
            data=request.data)
        errors = self.validate_serializer(serialized_data)
        if errors:
            return errors
        response = BussinessService().delete_business(request=request, **serialized_data.validated_data)

        return self.response(response)
    
    @action(detail=False, methods=["get"], url_path="fetch", permission_classes=[IsAuthenticated])
    @transaction.atomic
    def delete_business(self, request):
        serialized_data = inline_serializer(
            fields={
    "shop_name" : serializers.CharField(max_length=255, required=False),
            },
            data=request.data)
        errors = self.validate_serializer(serialized_data)
        if errors:
            return errors
        response = BussinessService().fetch_business(request=request, **serialized_data.validated_data)

        return self.response(response)
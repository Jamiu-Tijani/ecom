from django.db import models
from cloudinary.models import CloudinaryField
from accounts.models import Timestamp, Customer
from .choices import *
# Create your models here.

class Business(Timestamp):
    owner = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name="businesses")
    seller_id = models.UUIDField(auto_created=True)
    shop_name = models.CharField(max_length=255)
    contact_address = models.TextField(max_length=1000)
    postal_code = models.CharField(max_length=10)
    business_type = models.CharField(choices=BUSINESS_TYPE,max_length=20)
    full_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    extra_phone_number = models.CharField(max_length=20)
    legal_id = CloudinaryField('image')
    referrer = models.EmailField(max_length=50)
    no_of_employees = models.CharField(choices=EMPLOYEES,max_length=20)
    business_reg_number = models.CharField(max_length=255,null=True)
    registeration_certificate = CloudinaryField('image')
    legal_entity_country = models.CharField(max_length=255)
    shipping_country = models.CharField(max_length=255)

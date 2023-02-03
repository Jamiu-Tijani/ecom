from django.db import models
from cloudinary.models import CloudinaryField
from accounts.models import Timestamp, Customer
from .choices import *
import uuid
# Create your models here.

class Business(Timestamp):
    owner = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name="businesses")
    seller_id =models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    shop_name = models.CharField(max_length=255)
    contact_address = models.TextField(max_length=1000)
    postal_code = models.CharField(max_length=10)
    business_type = models.CharField(choices=BUSINESS_TYPE,max_length=20)
    full_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    extra_phone_number = models.CharField(max_length=20,null=True)
    referrer = models.EmailField(max_length=50,null=True)
    no_of_employees = models.CharField(choices=EMPLOYEES,max_length=20)
    business_reg_number = models.CharField(max_length=255,null=True)
    legal_entity_country = models.CharField(max_length=255,null=True)
    shipping_country = models.CharField(max_length=255)
    
    def __str__(self) -> str:
        return str(self.shop_name)

class BussinessLegalId(Timestamp):
    business =  models.ForeignKey(Business, on_delete=models.CASCADE, related_name="legal_id")
    legal_id = CloudinaryField('image', blank=True, null=True)
    verification_status = models.BooleanField(default=False)

    @property
    def image_url(self):
        return self.legal_id.url

class BussinessRegisterationCertificate(models.Model):
    business =  models.ForeignKey(Business, on_delete=models.CASCADE, related_name="reg_cert")
    registeration_certificate = CloudinaryField('image',blank=True,null=True)
    verification_status = models.BooleanField(default=False)
    
    @property
    def image_url(self):
        return self.registeration_certificate.url
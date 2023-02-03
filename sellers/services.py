from .models import Business,BussinessLegalId,BussinessRegisterationCertificate
from accounts.models import Customer
from accounts.constants import ErrorMessages,SuccessMessages
from django.db.models import Q

class BussinessService:
    def __init__(self):
        self.customer = Customer
        self.business = Business
        self.certificate_model = BussinessRegisterationCertificate
        self.legal_id_model = BussinessLegalId

    
    def validate_shop_name(self,shop_name):

        return self.business.objects.filter(shop_name=shop_name).exists()
        
    
    def create_business(self, request, **kwargs):
        shop_name = kwargs.get("shop_name")
        shop_exists = self.validate_shop_name(shop_name)
        if shop_exists:
            return dict(error=ErrorMessages.USER_ALREADY_EXISTS, status=409)
        customer = self.customer.objects.get(email=request.user.email)
        customer.is_seller = True
        customer.save()
        legal_id = None
        registeration_certificate = None
        if kwargs.get("legal_id"):
            legal_id = kwargs.get("legal_id")
            kwargs.pop("legal_id")
        if kwargs.get("registeration_certificate"):
            registeration_certificate = kwargs.get("registeration_certificate")
            kwargs.pop("registeration_certificate")
        business = self.business.objects.create(owner=customer,**kwargs)
        business.save()
        if registeration_certificate is not None:
            certificate_instance = self.certificate_model.objects.create(business=business,registeration_certificate=registeration_certificate)
            certificate_instance.save()
        if legal_id is not None:
            legal_id_instance = self.legal_id_model.objects.create(business=business,legal_id=legal_id)
            legal_id_instance.save()
        
        business_dict = {x:business.__dict__[x] for x in business.__dict__ if x[0]!= "_" }
        return dict(success=SuccessMessages.BUSINESS_CREATE_SUCCESSFUL , data=business_dict)

    def update_business(self, request, **kwargs):
        shop_name = kwargs.get("shop_name")
        customer = self.customer.objects.get(email=request.user.email)
        business = self.business.objects.get(shop_name=shop_name) 
        legal_id = None
        registeration_certificate = None
        shop_exists = self.validate_shop_name(shop_name)
        if kwargs.get("legal_id"):
            legal_id = kwargs.get("legal_id")
            kwargs.pop("legal_id")
        
        if kwargs.get("registeration_certificate"):
            registeration_certificate = kwargs.get("registeration_certificate")
            kwargs.pop("registeration_certificate")
        
        if not shop_exists:
            return dict(error=ErrorMessages.SHOP_NOT_FOUND, status=404)
        
        business_dict = {x:business.__dict__[x] for x in business.__dict__ if x[0]!= "_" }

        if registeration_certificate is not None:
            certificate_instance = self.certificate_model.objects.create(business=business,registeration_certificate=registeration_certificate)
            certificate_instance.save()
            business_dict["reg_cert"] = certificate_instance.image_url
        
        if legal_id is not None:
            legal_id_instance = self.legal_id_model.objects.create(business=business,legal_id=legal_id)
            legal_id_instance.save()       
            business_dict["legal_id"] = legal_id_instance.image_url

        
        return dict(success=SuccessMessages.BUSINESS_CREATE_SUCCESSFUL , data=business_dict)
    def fetch_business(self, request, **kwargs):
    
        shop_name = None
        if kwargs.get("shop_name"):
            shop_name = kwargs.get("shop_name")
        if shop_name is not None:     
            shop_exists = self.validate_shop_name(shop_name)
            if not shop_exists:
                return dict(error=ErrorMessages.SHOP_NOT_FOUND , status=404)
            customer = self.customer.objects.get(email=request.user.email)
            business = self.business.objects.filter(Q(owner=customer)&Q(shop_name=shop_name))   
            business = [x for x in business][0]
            business_dict = {x:business.__dict__[x] for x in business.__dict__ if x[0]!= "_" }

            print(type(business)) 

            return dict(success=SuccessMessages.BUSINESS_FOUND , data=business_dict)   

        customer = self.customer.objects.get(email=request.user.email)
        businesses = self.business.objects.filter(owner=customer)
        businesses =[x for x in businesses]
        businesses_arr = []
        for x in businesses:
            obj = x.__dict__
            obj_dict = {y: str(obj[y]) for y in obj.keys() if y[0] != "_"}
            businesses_arr.append(obj_dict)
            
        return dict(success=SuccessMessages.BUSINESS_FOUND , data=businesses_arr)   

    def delete_business(self, request, **kwargs):
        shop_name = kwargs.get("shop_name")
        customer = self.customer.objects.get(email=request.user.email)
        business = self.business.objects.filter(Q(owner=customer),Q(shop_name=shop_name)) 
        if not business.exists():
            return dict(error=ErrorMessages.SHOP_NOT_FOUND, status=404)
        business.delete()
        return dict(success=SuccessMessages.BUSINESS_CREATE_SUCCESSFUL , data={})
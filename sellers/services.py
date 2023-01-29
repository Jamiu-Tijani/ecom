from .models import Business
from accounts.models import Customer
from accounts.constants import ErrorMessages,SuccessMessages

class BussinessService:
    def __init__(self):
        self.customer = Customer
        self.business = Business
    
    def validate_shop_name(self,shop_name):

        return self.business.objects.filter(shop_name=shop_name).exists()
        
    
    def create_business(self, request, **kwargs):
        shop_name = kwargs.get("shop_name")
        shop_exists = self.validate_shop_name(shop_name)
        if shop_exists:
            return dict(error=ErrorMessages.USER_ALREADY_EXISTS, status=409)
        customer = self.customer.objects.get(email=request.user.email)
        business = self.business.objects.create(customer=customer,**kwargs)
        business.save()
        business_dict = {x:business.__dict__[x] for x in business.__dict__ if x[0]!= "_" }
        return dict(success=SuccessMessages.BUSINESS_CREATE_SUCCESSFUL , data=business_dict)
    
        

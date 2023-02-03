from accounts.constants import ErrorMessages,SuccessMessages
from django.db.models import Q
from .models import Product,ProductFeature,Category,ProductPrice
from sellers.models import Business
from sellers.services import BussinessService


class ProductService:
    def __init__(self):
        self.business_model = Business
        self.product_model = Product
        self.feature_model = ProductFeature
        self.category_model = Category

    def category(self, category):
        if self.category_model.objects.filter(name=category).exists():
            existing_category = [x for x in self.category_model.objects.filter(name=category)]
            return existing_category[0]
        else:
            return None
    def feature_exist(self, product, feature):
        if self.feature_model.objects.filter(product=product).exists():
            return True,
        else:
            return False

    

    def create_product(self, request, **kwargs):
        shop_name = kwargs.get("shop_name")
        shop_exists = BussinessService().validate_shop_name(shop_name=shop_name)
        print(kwargs.get("features"))

        if not shop_exists:
            return dict(error=ErrorMessages.SHOP_NOT_FOUND, status=404)
        category_name = kwargs.get("category")
        shop = self.business_model.objects.get(shop_name=shop_name)
        category = self.category(category=category_name)
        # category_parent = self.category(category=category_name)
        if category is None:
            if kwargs.get("category_parent"):
                print("Working 2")
                category_parent =  self.category_model.objects.get_or_create(name = kwargs.get("category_parent"))
                category_parent =  category_parent
                category = self.category_model.objects.create(name=category_name,parent=category_parent)
                kwargs.pop("category_parent")
                category.save()
            else:
                print("Working 3")
                category = self.category_model.objects.create(name=category_name)
                category.save()

        kwargs.pop("shop_name")
        kwargs.pop("features")
        price = kwargs.get("price")
        kwargs.pop("price")
        kwargs.pop("category")
        kwargs.pop("category_parent")
        # category = self.category_model.objects.get(name=category_name)
        product = self.product_model.objects.get_or_create(seller=shop,category=category, **kwargs)
        if product[1] == True:
            price = ProductPrice.objects.create(product=product[0],base_price = price)
        else:
            price = ProductPrice.objects.create(product=product[0],base_price = price)
        


        return dict(success="Product Creation SuccessFul" , data={})

    def retrieve_business_products(self, request, **kwargs):
        shop_name = kwargs.get("shop_name")
        shop_exists = BussinessService().validate_shop_name(shop_name=shop_name)

        if not shop_exists:
            return dict(error=ErrorMessages.SHOP_NOT_FOUND, status=404)
        print("Working")
        business=self.business_model.objects.get(shop_name=shop_name)
        queryset = self.product_model.objects.filter(seller=business)
        products =[x for x in queryset]
        products_arr = []
        for x in products:
            image = x.image_url
            category_parent = x.category.parent
            category = x.category
            obj = x.__dict__
            obj["image"] = image
            obj["category"] = category
            obj["category_parent"] = category_parent
            obj_dict = {y: str(obj[y]) for y in obj.keys() if y[0] != "_"}
            products_arr.append(obj_dict)

        return dict(success=SuccessMessages.BUSINESS_CREATE_SUCCESSFUL ,paginated=True, data=products_arr)





    


        

        
        
        
        
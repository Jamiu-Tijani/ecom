from django.db import models
import uuid
from mptt.models import MPTTModel, TreeForeignKey
from cloudinary.models import CloudinaryField
from sellers.models import Business,Timestamp


class Extensions(models.Model):
    """ Best practice for lookup field url instead pk or slug """

    uuid = models.UUIDField(db_index=True, default=uuid.uuid4, editable=False)
    created = models.DateTimeField(auto_now_add=True, db_index=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

# Create your models here.
class Category(MPTTModel):
    name = models.CharField(max_length=200)
    icon = CloudinaryField('image',null=True,blank=True)
    parent = TreeForeignKey(
        "self", null=True, blank=True, related_name="children", on_delete=models.CASCADE
    )
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Categories"

    class MPTTMeta:
        order_insertion_by = ['name']


    def __str__(self):
        return self.name


class Product(Extensions):
    seller = models.ForeignKey(
        Business, related_name="user_product", on_delete=models.CASCADE
    )
    category = TreeForeignKey(
        Category, related_name="product_category", on_delete=models.CASCADE
    )
    title = models.CharField(max_length=250)
    image = CloudinaryField('image')
    description = models.TextField(null=True, blank=True)
    quantity = models.IntegerField(default=1)
    views = models.IntegerField(default=0)
    is_deleted = models.BooleanField(default=False)

    @property
    def image_url(self):
        return self.image.url

    def __str__(self):
        return str(self.uuid)

class ProductPrice(Extensions):
    product = models.ForeignKey(
        Product, related_name="user_product", on_delete=models.CASCADE
    )
    base_price = models.DecimalField(decimal_places=2, max_digits=10, null=True, blank=True)
    discounted_price = models.DecimalField(decimal_places=2, max_digits=10, null=True, blank=True)

    def __str__(self):
        return self.product.title


class ProductFeature(models.Model):
    product = models.ForeignKey(Product, related_name="features", on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    value = models.CharField(max_length=250)
    descr = models.TextField(max_length=1000, null=True)

    def __str__(self):
        return self.name

class ProductViews(Timestamp):
    ip = models.CharField(max_length=250)
    product = models.ForeignKey(
        Product, related_name="product_views", on_delete=models.CASCADE
    )

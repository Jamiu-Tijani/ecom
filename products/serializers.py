from rest_framework import serializers
from .models import ProductFeature, Category, Product,ProductViews
# import serpy
# from sellers.models import Business
# from .documents import ProductDocument
# from .search_indexes import ProductIndex
# from drf_extra_fields.fields import Base64ImageField
# from drf_haystack.serializers import HaystackSerializer
# from django_elasticsearch_dsl_drf.serializers import DocumentSerializer


class ProductFeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductFeature
        fields = ['name', 'value', 'descr']

# class ProductFeaturesSerializer(serializers.ModelSerializer):
#     features = ProductFeatureSerializer(many=True)
#     class Meta:
#         fields = ["features"]
#         model = ProductFeature

# # class ProductFeatureNameSerializer(serializers.ModelSerializer):
# #     class Meta:
# #         model = ProductFeature
# #         fields = ('name', 'value', 'descr')


# class ProductDocumentSerializer(DocumentSerializer):
#     seller = serializers.SlugRelatedField(slug_field="shop_name", queryset=Business.objects)
#     category = serializers.SerializerMethodField()

#     def get_category(self, obj):
#         return obj.category.name

#     class Meta(object):
#         # model = Product
#         document = ProductDocument
#         exclude = ["modified"]


# class ProductIndexSerializer(HaystackSerializer):
#     class Meta:
#         # The `index_classes` attribute is a list of which search indexes
#         # we want to include in the search.
#         index_classes = [ProductIndex]

#         # The `fields` contains all the fields we want to include.
#         # NOTE: Make sure you don't confuse these with model attributes. These
#         # fields belong to the search index!
#         fields = ("text", "title", "category",)

# class CategoryListSerializer(serializers.ModelSerializer):
#     # lft = serializers.SlugRelatedField(slug_field='lft', read_only=True)
#     class Meta:
#         model = Category
#         exclude = ["modified"]


# class ProductSerializer(serializers.ModelSerializer):
#     seller = serializers.SlugRelatedField(slug_field="shop_name", queryset=Business.objects, required=False)
#     shop_name = serializers.CharField(max_length=200,required=False)
#     category = serializers.SerializerMethodField(required=False)
#     title = serializers.CharField(max_length=200,required=False)
#     image = serializers.ImageField(required=False)


#     def get_category(self, obj):
#         return obj.category.name

#     class Meta:
#         model = Product
#         exclude = ["modified"]


# class SerpyProductSerializer(serpy.Serializer):
#     seller = serpy.StrField()
#     category = serpy.StrField()
#     title = serpy.StrField()
#     price = serpy.FloatField()
#     image = serpy.StrField()
#     description = serpy.StrField()
#     quantity = serpy.IntField()
#     views = serpy.IntField()


# class ProductMiniSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Product
#         fields = ["title"]

#     def to_representation(self, instance):
#         data = super().to_representation(instance)
#         data = serializers.ModelSerializer.to_representation(self, instance)
#         return data


# class CreateProductSerializer(serializers.ModelSerializer):
#     features = ProductFeatureSerializer(many=True)
#     class Meta:
#         model = Product
#         exclude = ("modified",)
#         # read_only_fields = ('id', 'seller', 'category', 'title', 'price', 'image', 'description', 'quantity', 'views',)


# class ProductDetailSerializer(serializers.ModelSerializer):
#     seller = serializers.SlugRelatedField(slug_field="shop_name", queryset=Business.objects)
#     category = serializers.SerializerMethodField()
#     image = Base64ImageField()

#     def get_category(self, obj):
#         return obj.category.name

#     class Meta:
#         model = Product
#         exclude = ["modified"]


# class ProductViewsSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = ProductViews
#         exclude = ["modified"]
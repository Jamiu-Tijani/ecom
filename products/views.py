# from django.core.cache import cache
# from django.conf import settings
# from django.core.cache.backends.base import DEFAULT_TIMEOUT
# from django.utils.decorators import method_decorator
# from django.views.decorators.cache import cache_page
# from django.views.decorators.vary import vary_on_cookie
# from django.utils.translation import ugettext_lazy as _
# from rest_framework import viewsets
# from accounts.constants import ErrorMessages
# from sellers.models import Business
# import logging
# from django_elasticsearch_dsl_drf.constants import LOOKUP_FILTER_GEO_DISTANCE
# from django_elasticsearch_dsl_drf.filter_backends import (
#     FilteringFilterBackend,
#     OrderingFilterBackend,
#     SearchFilterBackend,
#     DefaultOrderingFilterBackend,
# )
# from django.shortcuts import get_object_or_404

# from accounts.mixins import CustomResponseMixin

# from rest_framework import permissions
# from rest_framework.exceptions import PermissionDenied, NotAcceptable, ValidationError

# from django_elasticsearch_dsl_drf.viewsets import DocumentViewSet, BaseDocumentViewSet
# from django_filters.rest_framework import DjangoFilterBackend

# from .models import Category, Product, ProductViews
# from .serializers import (
#     CategoryListSerializer,
#     ProductSerializer,
#     SerpyProductSerializer,
#     CreateProductSerializer,
#     ProductViewsSerializer,
#     ProductDetailSerializer,
#     ProductMiniSerializer,
#     ProductDocumentSerializer,
# )
# from rest_framework.generics import (
#     ListAPIView,
#     RetrieveAPIView,
#     CreateAPIView,
#     DestroyAPIView,
# )
# from rest_framework.response import Response
# from rest_framework.views import APIView

# from .documents import ProductDocument
# from .permissions import IsOwnerAuth, ModelViewSetsPermission
# # from notifications.utils import push_notifications
# # from notifications.twilio import send_message
# from .decorators import time_calculator
# from django_elasticsearch_dsl_drf.constants import LOOKUP_FILTER_GEO_DISTANCE
# from django_elasticsearch_dsl_drf.filter_backends import (
#     FilteringFilterBackend,
#     OrderingFilterBackend,
#     SearchFilterBackend,
#     DefaultOrderingFilterBackend,
# )
# from rest_framework import viewsets

# from rest_framework import filters

# from django_elasticsearch_dsl_drf.viewsets import DocumentViewSet, BaseDocumentViewSet

# from googletrans import Translator

# translator = Translator()
# logger = logging.getLogger(__name__)


# class SerpyListProductAPIView(ListAPIView):
#     serializer_class = SerpyProductSerializer
#     filter_backends = (
#         DjangoFilterBackend,
#         filters.SearchFilter,
#         filters.OrderingFilter,
#     )
#     search_fields = ("title",)
#     ordering_fields = ("created",)
#     filter_fields = ("views",)
#     queryset = Product.objects.all()

#     # def get_queryset(self):
#     #     import cProfile
#     #     from django.contrib.auth.models import User
#     #     u = User.objects.get(id=5)
#     #     p = Product.objects.create(seller=u, category=Category.objects.get(id=1), title='test', price=20, description='dsfdsfdsf', quantity=10)
#     #     cProfile.runctx('for i in range(5000): SerpyProductSerializer(p).data', globals(), locals(), sort='tottime')
#     #     queryset = Product.objects.all()
#     #     return queryset


# class ListProductView(viewsets.ModelViewSet):
#     permission_classes = (ModelViewSetsPermission,)
#     serializer_class = CreateProductSerializer
#     filter_backends = (
#         DjangoFilterBackend,
#         filters.SearchFilter,
#         filters.OrderingFilter,
#     )
#     search_fields = ("title",)
#     ordering_fields = ("created",)
#     filter_fields = ("views",)
#     queryset = Product.objects.all()

#     # def list(self, request, *args, **kwargs):
#     #     queryset = self.filter_queryset(self.get_queryset())
#     #     print("queryset -> ", queryset)
#     #     serializer = self.get_serializer(queryset, many=True)
#     #     return Response(serializer)

#     def update(self, request, *args, **kwargs):
#         from django.contrib.auth.models import User

#         if User.objects.get(username="tomas33") != self.get_object().seller:
#             raise NotAcceptable(_("you don't own product"))
#         return super(ListProductView, self).update(request, *args, **kwargs)


# class ProductDocumentView(DocumentViewSet):
#     document = ProductDocument
#     serializer_class = ProductDocumentSerializer
#     lookup_field = "id"
#     filter_backends = [
#         FilteringFilterBackend,
#         OrderingFilterBackend,
#         DefaultOrderingFilterBackend,
#         SearchFilterBackend,
#     ]
#     search_fields = ("title",)
#     filter_fields = {"title": "title.raw"}
#     ordering_fields = {"created": "created"}
#     # ordering = ('-created',)
#     queryset = Product.objects.all()


# class CategoryListAPIView(ListAPIView):
#     # permission_classes = [permissions.IsAuthenticated]
#     serializer_class = CategoryListSerializer
#     filter_backends = (
#         DjangoFilterBackend,
#         filters.SearchFilter,
#         filters.OrderingFilter,
#     )
#     search_fields = ("name",)
#     ordering_fields = ("created",)
#     filter_fields = ("created",)
#     # queryset = Category.objects.all()

#     @time_calculator
#     def time(self):
#         return 0

#     def get_queryset(self):
#         queryset = Category.objects.all()
#         self.time()
#         return queryset


# class CategoryAPIView(RetrieveAPIView):
#     # permission_classes = [permissions.IsAuthenticated]
#     serializer_class = CategoryListSerializer
#     queryset = Category.objects.all()

#     def retrieve(self, request, *args, **kwargs):
#         instance = self.get_object()
#         serializer = self.get_serializer(instance)
#         data = {}
#         for k, v in serializer.data.items():
#             data[k] = translator.translate(str(v), dest="ar").text

#         return Response(data)


# class ListProductAPIView(ListAPIView):
#     permission_classes = [permissions.AllowAny]
#     serializer_class = ProductSerializer
#     filter_backends = (
#         DjangoFilterBackend,
#         filters.SearchFilter,
#         filters.OrderingFilter,
#     )
#     search_fields = ("title",)
#     ordering_fields = ("created",)
#     filter_fields = ("views",)
#     queryset = Product.objects.all()

#     # def get_queryset(self):
#     #     import cProfile
#     #     from django.contrib.auth.models import User
#     #     u = User.objects.get(id=5)
#     #     p = Product.objects.create(seller=u, category=Category.objects.get(id=1), title='test', price=20, description='dsfdsfdsf', quantity=10)
#     #     cProfile.runctx('for i in range(5000): ProductSerializer(p).data', globals(), locals(), sort='tottime')
#     #     queryset = Product.objects.all()
#     #     return queryset

#     @time_calculator
#     def time(self):
#         return 0

#     # Cache requested url for each user for 2 hours
#     @method_decorator(cache_page(60 * 60 * 2))
#     @method_decorator(vary_on_cookie)
#     def list(self, request, *args, **kwargs):
#         queryset = self.filter_queryset(self.get_queryset())

#         page = self.paginate_queryset(queryset)
#         if page is not None:
#             serializer = self.get_serializer(page, many=True)
#             return self.get_paginated_response(serializer.data)

#         serializer = self.get_serializer(queryset, many=True)
#         self.time()
#         return Response(serializer.data)


# class ListBusinessProductAPIView(ListAPIView,CustomResponseMixin):
#     serializer_class = ProductSerializer
#     filter_backends = (
#         DjangoFilterBackend,
#         filters.SearchFilter,
#         filters.OrderingFilter,
#     )
#     search_fields = (
#         "title",
#         "business__shop_name",
#     )
#     ordering_fields = ("created",)
#     filter_fields = ("views",)

#     def get_queryset(self):
#         serializer = ProductSerializer(data=self.request.data)
#         if not serializer.is_valid():
#             raise ValidationError(_(f"Invalid Payload  {str(serializer.errors)}"))

#         user = self.request.user
#         business= Business.objects.get(shop_name=self.request.data["shop_name"])
#         queryset = Product.objects.select_related('seller').filter(seller=business)
#         return queryset


# class CreateProductAPIView(CreateAPIView,CustomResponseMixin):
#     permission_classes = [permissions.IsAuthenticated]
#     serializer_class = CreateProductSerializer

#     def create(self, request, *args, **kwargs):
#         user = request.user
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save(seller=user)
        
#         #push_notifications(user, request.data["title"], "you have add a new product")
#         # if user.profile.phone_number:
#         #     send_message(user.profile.phone_number, "Congratulations, you Created New Product")
#         logger.info(
#             "product ( "
#             + str(serializer.data.get("title"))
#             + " ) created"
#             + " by ( "
#             + str(user.username)
#             + " )"
#         )
#         return self.response(dict(success= "CREATED" ,data = serializer.data))


# class DestroyProductAPIView(DestroyAPIView):
#     permission_classes = [IsOwnerAuth]
#     serializer_class = ProductDetailSerializer
#     queryset = Product.objects.all()

#     def destroy(self, request, *args, **kwargs):
#         instance = self.get_object()
#         instance.is_deleted = True
#         instance.save()
#         return Response({"detail": "Product deleted"})


# class ProductViewsAPIView(ListAPIView):
#     # permission_classes = [IsOwnerAuth]
#     serializer_class = ProductViewsSerializer
#     queryset = ProductViews.objects.all()


# class ProductDetailView(APIView,CustomResponseMixin):
#     def get(self, request, uuid):
#         product = Product.objects.get(uuid=uuid)
#         x_forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR")
#         if x_forwarded_for:
#             ip = x_forwarded_for.split(",")[0]
#         else:
#             ip = request.META.get("REMOTE_ADDR")

#         if not ProductViews.objects.filter(product=product, ip=ip).exists():
#             ProductViews.objects.create(product=product, ip=ip)

#             product.views += 1
#             product.save()
#         serializer = ProductDetailSerializer(product, context={"request": request})

#         return self.response(dict(success= "CREATED" ,data = serializer.data))


#     def put(self, request, pk):
#         user = request.user
#         product = get_object_or_404(Product, pk=pk)
#         if product.user != user:
#             raise PermissionDenied("this product don't belong to you.")

#         serializer = ProductDetailSerializer(
#             product, data=request.data, context={"request": request}
#         )
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)
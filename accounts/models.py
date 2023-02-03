from django.db import models
from django.contrib.auth.models import User
import uuid
# from apps.models import Timestamp


class Timestamp(models.Model):
    """
    Timestamp mixin to inherit
    """

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    # prevent dj from creating a column for this table
    class Meta:
        abstract = True


class Customer(User, Timestamp):
    owner_id = models.UUIDField(default=uuid.uuid4, editable=False)
    is_seller = models.BooleanField(default=False)


    def __str__(self):
        return f'{self.username}'




# this model Stores the data of the emails verified
class EmailToken(models.Model):
    email = models.CharField(max_length=80, null=True, blank=True)
    is_verified = models.BooleanField(blank=False, default=False)

    def __str__(self):
        return str(self.email)

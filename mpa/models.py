from django.db import models
import pickle as p
from rest_framework import serializers

class SerializedField(serializers.ModelSerializer):
    """
    使用pickle来实现存储 Python 对象
    """
    __metaclass__ = models



# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=50, null=False, unique=True)
    email = models.CharField(max_length=100, null=True)
    password = models.TextField(max_length=50)
    create_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

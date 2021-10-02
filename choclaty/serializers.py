from django.db.models.fields import Field
from django.http import request
from rest_framework import serializers
from home.models import Form

class FormSerializer(serializers.HyperlinkedModelSerializer): 
    
    class Meta:
        model = Form
        fields =  ('name', 'email', 'city', 'mobile')


# class FormSerializer(serializers.HyperlinkedModelSerializer): 
#     name = serializers.CharField(max_length=122)
#     mobile = serializers.CharField(max_length=12)
#     email = serializers.CharField(max_length=50)
#     city = serializers.CharField(max_length=50)
              
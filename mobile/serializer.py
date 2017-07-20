__author__ = 'Amad'
from rest_framework import serializers

from .models import Mobile_DB
from drf_extra_fields.fields import Base64ImageField
from django.core.paginator import Paginator

class Mobile_Serializer(serializers.ModelSerializer):
    # SNR_Thumbnail = Base64ImageField(required=False,use_url=True)

    class Meta:
        model=Mobile_DB
        fields = ('SNR_SKU', 'SNR_Title', 'SNR_ModelNo', 'SNR_Brand', 'SNR_UPC', 'SNR_Price', 'SNR_Available', 'SNR_ProductURL', 'SNR_ImageURL', 'SNR_Description')


class Mobile_SerializerTitle(serializers.ModelSerializer):
    # SNR_Thumbnail = Base64ImageField(required=False,use_url=True)

    class Meta:
        model=Mobile_DB
        fields = ('SNR_Title','SNR_UPC','SNR_ModelNo')

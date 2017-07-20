__author__ = 'Amad'
from rest_framework import serializers

from .models import Trends

class TrendsSerializer(serializers.ModelSerializer):

    class Meta:
        model=Trends
        fields=('SNR_Title','SNR_Description','SNR_PriceMin','SNR_PriceMax','SNR_ProductURL' ,'SNR_ImageURL','SNR_AvailableAt','SNR_Type','SNR_Category')

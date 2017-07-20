from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from .models import TV,Cams,CarsElectronics,VideoGames,Toys,SmartHomes,Audio,ComputerSoftware,Applinces,Movies,OfficeSupply,HealthandFitness
from drf_extra_fields.fields import Base64ImageField



class Software_SerializerTitle(serializers.ModelSerializer):

    class Meta:

        model = ComputerSoftware
        fields = ('SNR_Title', 'SNR_UPC', 'SNR_ModelNo')


class Health_SerializerTitle(serializers.ModelSerializer):

    class Meta:

        model = HealthandFitness
        fields = ('SNR_Title', 'SNR_UPC', 'SNR_ModelNo')


class Office_SerializerTitle(serializers.ModelSerializer):

    class Meta:

        model = OfficeSupply
        fields = ('SNR_Title', 'SNR_UPC', 'SNR_ModelNo')


class Movies_SerializerTitle(serializers.ModelSerializer):

    class Meta:

        model = Movies
        fields = ('SNR_Title', 'SNR_UPC', 'SNR_ModelNo')


class Applinces_SerializerTitle(serializers.ModelSerializer):

    class Meta:

        model = Applinces
        fields = ('SNR_Title', 'SNR_UPC', 'SNR_ModelNo')


class TV_SerializerTitle(serializers.ModelSerializer):

    class Meta:

        model = TV
        fields = ('SNR_Title', 'SNR_UPC', 'SNR_ModelNo')


class Cams_SerializerTitle(serializers.ModelSerializer):

    class Meta:

        model = Cams
        fields = ('SNR_Title', 'SNR_UPC', 'SNR_ModelNo')


class CarsElec_SerializerTitle(serializers.ModelSerializer):

    class Meta:

        model = CarsElectronics
        fields = ('SNR_Title', 'SNR_UPC', 'SNR_ModelNo')


class VideoGames_SerializerTitle(serializers.ModelSerializer):

    class Meta:

        model = VideoGames
        fields = ('SNR_Title', 'SNR_UPC', 'SNR_ModelNo')


class Toys_SerializerTitle(serializers.ModelSerializer):

    class Meta:

        model = Toys
        fields = ('SNR_Title', 'SNR_UPC', 'SNR_ModelNo')


class Smarthomes_SerializerTitle(serializers.ModelSerializer):

    class Meta:

        model = SmartHomes
        fields = ('SNR_Title', 'SNR_UPC', 'SNR_ModelNo')


class Audio_SerializerTitle(serializers.ModelSerializer):

    class Meta:

        model = Audio
        fields = ('SNR_Title', 'SNR_UPC', 'SNR_ModelNo')


class Software_Serializer(serializers.ModelSerializer):

    class Meta:

        model = ComputerSoftware
        fields=('SNR_Title','SNR_Brand','SNR_Description','SNR_ImageURL','SNR_ModelNo','SNR_UPC','SNR_SKU','SNR_ProductURL','SNR_Price','SNR_Available')



class Health_Serializer(serializers.ModelSerializer):

    class Meta:

        model = HealthandFitness
        fields=('SNR_Title','SNR_Brand','SNR_Description','SNR_ImageURL','SNR_ModelNo','SNR_UPC','SNR_SKU','SNR_ProductURL','SNR_Price','SNR_Available')


class Office_Serializer(serializers.ModelSerializer):

    class Meta:

        model = OfficeSupply
        fields=('SNR_Title','SNR_Brand','SNR_Description','SNR_ImageURL','SNR_ModelNo','SNR_UPC','SNR_SKU','SNR_ProductURL','SNR_Price','SNR_Available')





class Movies_Serializer(serializers.ModelSerializer):

    class Meta:

        model = Movies
        fields=('SNR_Title','SNR_Brand','SNR_Description','SNR_ImageURL','SNR_ModelNo','SNR_UPC','SNR_SKU','SNR_ProductURL','SNR_Price','SNR_Available')



class Applinces_Serializer(serializers.ModelSerializer):

    class Meta:

        model = Applinces
        fields=('SNR_Title','SNR_Brand','SNR_Description','SNR_ImageURL','SNR_ModelNo','SNR_UPC','SNR_SKU','SNR_ProductURL','SNR_Price','SNR_Available')


class TV_Serializer(serializers.ModelSerializer):

    class Meta:

        model = TV
        fields=('SNR_Title','SNR_Brand','SNR_Description','SNR_ImageURL','SNR_ModelNo','SNR_UPC','SNR_SKU','SNR_ProductURL','SNR_Price','SNR_Available')


class Cams_Serializer(serializers.ModelSerializer):

    class Meta:

        model = Cams
        fields=('SNR_Title','SNR_Brand','SNR_Description','SNR_ImageURL','SNR_ModelNo','SNR_UPC','SNR_SKU','SNR_ProductURL','SNR_Price','SNR_Available')


class CarsElec_Serializer(serializers.ModelSerializer):

    class Meta:

        model = CarsElectronics
        fields=('SNR_Title','SNR_Brand','SNR_Description','SNR_ImageURL','SNR_ModelNo','SNR_UPC','SNR_SKU','SNR_ProductURL','SNR_Price','SNR_Available')


class VideoGames_Serializer(serializers.ModelSerializer):

    class Meta:

        model = VideoGames
        fields=('SNR_Title','SNR_Brand','SNR_Description','SNR_ImageURL','SNR_ModelNo','SNR_UPC','SNR_SKU','SNR_ProductURL','SNR_Price','SNR_Available')


class Toys_Serializer(serializers.ModelSerializer):

    class Meta:

        model = Toys
        fields=('SNR_Title','SNR_Brand','SNR_Description','SNR_ImageURL','SNR_ModelNo','SNR_UPC','SNR_SKU','SNR_ProductURL','SNR_Price','SNR_Available')


class Smarthomes_Serializer(serializers.ModelSerializer):

    class Meta:

        model = SmartHomes
        fields=('SNR_Title','SNR_Brand','SNR_Description','SNR_ImageURL','SNR_ModelNo','SNR_UPC','SNR_SKU','SNR_ProductURL','SNR_Price','SNR_Available')


class Audio_Serializer(serializers.ModelSerializer):

    class Meta:

        model = Audio
        fields=('SNR_Title','SNR_Brand','SNR_Description','SNR_ImageURL','SNR_ModelNo','SNR_UPC','SNR_SKU','SNR_ProductURL','SNR_Price','SNR_Available')



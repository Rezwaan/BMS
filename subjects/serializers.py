from rest_framework import serializers
from .models import pp_subjects

class pp_subjectsSerializer(serializers.ModelSerializer):

    class Meta:
        model = pp_subjects
        #fields = ('subject_name', 'subject_age', 'psd1', 'psd3', 'psd6', 'psd10')
        fields = '__all__'

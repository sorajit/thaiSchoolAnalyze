from rest_framework import serializers
from .models import  SchoolData

class SchoolDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = SchoolData
        fields = '__all__'
        # ('geom','sector','subdistrict','district','province','county','group','village','post_office','lat','lng')

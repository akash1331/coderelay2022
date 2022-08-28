from rest_framework import serializers
from codeapp.models import *

class dataSerializer(serializers.ModelSerializer):
    class Meta():
        model = itemdata
        fields = '__all__'

class typeSerializer(serializers.ModelSerializer):
    class Meta():
        model = itemstype
        fields = '__all__'
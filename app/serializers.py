from rest_framework import serializers
from .models import PointOfSale, Visit


class PointOfSaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = PointOfSale
        fields = ['id', 'name', 'employee']


class VisitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visit
        fields = ['id', 'datetime', 'point_of_sale', 'latitude', 'longitude']

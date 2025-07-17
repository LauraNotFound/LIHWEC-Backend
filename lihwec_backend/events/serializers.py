from rest_framework import serializers
from .models import Event, Organization, Category

class EventSerializer(serializers.ModelSerializer):
    organization = serializers.CharField(source='organization.name', read_only=True)
    category = serializers.CharField(source='category.name', read_only=True)

    class Meta:
        model = Event
        fields = '__all__'

class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
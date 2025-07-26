from rest_framework import serializers
from .models import Event, Organization, Category, Type

class EventSerializer(serializers.ModelSerializer):
    organization = serializers.SlugRelatedField(
        slug_field='name',
        queryset=Organization.objects.all()
    )
    category = serializers.SlugRelatedField(
        slug_field='name',
        queryset=Category.objects.all()
    )
    type = serializers.SlugRelatedField(
        slug_field='name',
        queryset=Type.objects.all()
    )

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

class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = '__all__'
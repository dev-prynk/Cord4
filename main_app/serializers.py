from rest_framework import serializers
from .models import event_table, EventCategory, EventOrganiser


class EventCategory_Serializer(serializers.ModelSerializer):
    class Meta:
        model = EventCategory
        fields = '__all__'

class EventOrganiser_Serializer(serializers.ModelSerializer):
    class Meta:
        model = EventOrganiser
        fields = '__all__'

class Event_Serializer(serializers.ModelSerializer):

    
    organiser = EventOrganiser_Serializer()
    category = EventCategory_Serializer()

    organiser = serializers.PrimaryKeyRelatedField(queryset=EventOrganiser.objects.all())
    category = serializers.PrimaryKeyRelatedField(queryset=EventCategory.objects.all())

    class Meta:
        model = event_table
        fields = ["title","description","date","organiser","category"]
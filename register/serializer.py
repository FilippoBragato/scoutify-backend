from rest_framework import serializers
from .models import Activity, ScoutPartecipation
from scout.serializer import ScoutPatrolSerializer

class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = '__all__'

class ScoutPartecipationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScoutPartecipation
        fields = '__all__'

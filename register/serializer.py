from rest_framework import serializers
from .models import Activity, ScoutPartecipation
from scout.serializer import ScoutPatrolSerializer

class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = '__all__'

class ScoutPartecipationSerializer(serializers.ModelSerializer):
    scout = ScoutPatrolSerializer()
    activity = ActivitySerializer()
    class Meta:
        model = ScoutPartecipation
        fields = ['id', 'date', 'scout', 'activity', 'justification']

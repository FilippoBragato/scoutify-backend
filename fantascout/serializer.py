from rest_framework import serializers
from .models import FantaTask, ScoutCompleteTask
from scout.serializer import ScoutPatrolSerializer

class FantaTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = FantaTask
        fields = '__all__'

class ScoutCompleteTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScoutCompleteTask
        fields = '__all__'

class JoinScoutCompleteTaskSerializer(serializers.ModelSerializer):
    scout = ScoutPatrolSerializer()
    task = FantaTaskSerializer()
    class Meta:
        model = ScoutCompleteTask
        fields = ['id', 'date','scout', 'task', 'checked']
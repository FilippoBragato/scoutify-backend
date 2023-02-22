from rest_framework import serializers
from .models import FantaTask, ScoutCompleteTask

class FantaTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = FantaTask
        fields = '__all__'

class ScoutCompleteTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScoutCompleteTask
        fields = '__all__'
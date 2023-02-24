from rest_framework import serializers
from .models import Scout, Patrol

class ScoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Scout
        fields = '__all__'

class PatrolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patrol
        fields = '__all__'

class ScoutPatrolSerializer(serializers.ModelSerializer):
    patrol = PatrolSerializer()
    class Meta:
        model = Scout
        fields = ['id', 'user', 'name', 'patrol', 'verified','birthday']
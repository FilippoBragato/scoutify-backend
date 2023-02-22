from rest_framework import serializers
from .models import Scout, Patrol

class ScoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Scout
        fields = ('user', 'id', 'birthday', 'patrol', 'verified')

class PatrolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patrol
        fields = '__all__'
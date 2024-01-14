from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializer import ActivitySerializer, ScoutPartecipationSerializer
from .models import Activity, ScoutPartecipation
from scout.serializer import ScoutPatrolSerializer
from django.contrib.auth.models import User
from datetime import datetime

# rest for Activity
@api_view(['GET'])
def getAllActivity(request):
    if request.user.is_authenticated:
        if request.user.has_perm('register.view_activity'):
            activity = Activity.objects.all()
            serializer = ActivitySerializer(activity, many=True)
            return Response(serializer.data)
    return Response({'error': 'You should not be here'}, status=401)

@api_view(['POST'])
def addActivity(request):
    if request.user.is_authenticated:
        if request.user.has_perm('register.add_activity'):
            serializer = ActivitySerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
            return Response(serializer.data)
    return Response({'error': 'You should not be here'}, status=401)

@api_view(['PUT'])
def editActivity(request, pk):
    if request.user.is_authenticated:
        if request.user.has_perm('register.change_activity'):
            try:
                task = Activity.objects.get(pk=pk)
            except Activity.DoesNotExist:
                return Response(status=404)
            serializer = ActivitySerializer(task, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=400)
    return Response({'error': 'You should not be here'}, status=401)

@api_view(['DELETE'])
def deleteActivity(request, pk):
    if request.user.is_authenticated:
        if request.user.has_perm('register.delete_activity'):
            try:
                task = Activity.objects.get(pk=pk)
            except Activity.DoesNotExist:
                return Response(status=404)
            serializer = ActivitySerializer(task)
            task.delete()
            return Response(serializer.data)
    return Response({'error': 'You should not be here'}, status=401)

# rest for ScoutPartecipation
@api_view(['GET'])
def getAllScoutPartecipation(request):
    if request.user.is_authenticated:
        if request.user.has_perm('register.view_scoutpartecipation'):
            scoutPartecipation = ScoutPartecipation.objects.all()
            serializer = ScoutPartecipationSerializer(scoutPartecipation, many=True)
            return Response(serializer.data)
    return Response({'error': 'You should not be here'}, status=401)

@api_view(['POST'])
def addScoutPartecipation(request):
    if request.user.is_authenticated:
        if request.user.has_perm('register.add_scoutpartecipation'):
            scout_id = request.data.get('scout_id')
            activity_id = request.data.get('activity_id')
            try:
                scout_participation = ScoutPartecipation.objects.get(scout_id=scout_id, activity_id=activity_id)
                serializer = ScoutPartecipationSerializer(scout_participation, data=request.data)
                if serializer.is_valid():
                    serializer.save(time=datetime.now())  # Update the time
                    return Response(serializer.data)
                return Response(serializer.errors, status=400)
            except ScoutPartecipation.DoesNotExist:
                serializer = ScoutPartecipationSerializer(data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data)
                return Response(serializer.errors, status=400)
    return Response({'error': 'You should not be here'}, status=401)

@api_view(['PUT'])
def editScoutPartecipation(request, pk):
    if request.user.is_authenticated:
        if request.user.has_perm('register.change_scoutpartecipation'):
            try:
                task = ScoutPartecipation.objects.get(pk=pk)
            except ScoutPartecipation.DoesNotExist:
                return Response(status=404)
            serializer = ScoutPartecipationSerializer(task, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=400)
    return Response({'error': 'You should not be here'}, status=401)

@api_view(['DELETE'])
def deleteScoutPartecipation(request, pk):
    if request.user.is_authenticated:
        if request.user.has_perm('register.delete_scoutpartecipation'):
            try:
                task = ScoutPartecipation.objects.get(pk=pk)
            except ScoutPartecipation.DoesNotExist:
                return Response(status=404)
            serializer = ScoutPartecipationSerializer(task)
            task.delete()
            return Response(serializer.data)
    return Response({'error': 'You should not be here'}, status=401)

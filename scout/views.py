from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializer import ScoutSerializer, PatrolSerializer
from .models import Scout, Patrol
from django.contrib.auth.models import User

# REST FOR SCOUT
@api_view(['GET'])
def getAllScout(request):
    if request.user.is_authenticated:
        if request.user.has_perm('scout.view_scout'):
            scout = Scout.objects.all()
            serializer = ScoutSerializer(scout, many=True)
            return Response(serializer.data)
    return Response({'error': 'You should not be here'}, status=401)

@api_view(['POST'])
def addScout(request):
    if request.user.is_authenticated:
        if request.user.has_perm('scout.add_scout'):
            serializer = ScoutSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
            return Response(serializer.data)
    return Response({'error': 'You should not be here'}, status=401)

@api_view(['PUT'])
def editScout(request, pk):
    if request.user.is_authenticated:
        if request.user.has_perm('scout.change_scout'):
            try:
                task = Scout.objects.get(pk=pk)
            except Scout.DoesNotExist:
                return Response(status=404)
            serializer = ScoutSerializer(task, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=400)
    return Response({'error': 'You should not be here'}, status=401)

@api_view(['DELETE'])
def deleteScout(request, pk):
    if request.user.is_authenticated:
        if request.user.has_perm('scout.delete_scout'):
            try:
                task = Scout.objects.get(pk=pk)
            except Scout.DoesNotExist:
                return Response(status=404)
            serializer = ScoutSerializer(task)
            task.delete()
            return Response(serializer.data)
    return Response({'error': 'You should not be here'}, status=401)

# REST FOR PATROL
@api_view(['GET'])
def getAllPatrols(request):
    if request.user.is_authenticated:
        if request.user.has_perm('scout.view_patrol'):
            patrol = Patrol.objects.all()
            serializer = PatrolSerializer(patrol, many=True)
            return Response(serializer.data)
    return Response({'error': 'You should not be here'}, status=401)

@api_view(['GET'])
def getMyPatrol(request):
    if request.user.is_authenticated:
        if request.user.has_perm('scout.view_patrol'):
            my_scout = Scout.objects.filter(user=request.user.id)[0]
            my_patrol = Scout.objects.filter(patrol=my_scout.patrol)
            serializer = ScoutSerializer(my_patrol, many=True)
            return Response(serializer.data)
        else:
            return Response({'error': 'You should not be here'}, status=401)
    else:
        return Response({'error': 'You should not be here'}, status=401)

@api_view(['POST'])
def addPatrol(request):
    if request.user.is_authenticated:
        if request.user.has_perm('scout.add_patrol'):
            serializer = PatrolSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
            return Response(serializer.data)
    return Response({'error': 'You should not be here'}, status=401)

@api_view(['PUT'])
def editPatrol(request, pk):
    if request.user.is_authenticated:
        if request.user.has_perm('scout.change_patrol'):
            try:
                task = Patrol.objects.get(pk=pk)
            except Patrol.DoesNotExist:
                return Response(status=404)
            serializer = PatrolSerializer(task, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=400)
    return Response({'error': 'You should not be here'}, status=401)

@api_view(['DELETE'])
def deletePatrol(request, pk):
    if request.user.is_authenticated:
        if request.user.has_perm('scout.delete_patrol'):
            try:
                task = Patrol.objects.get(pk=pk)
            except Patrol.DoesNotExist:
                return Response(status=404)
            serializer = PatrolSerializer(task)
            task.delete()
            return Response(serializer.data)
    return Response({'error': 'You should not be here'}, status=401)
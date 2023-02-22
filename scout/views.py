from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializer import ScoutSerializer, PatrolSerializer
from .models import Scout, Patrol

# REST FOR SCOUT
@api_view(['GET'])
def getAllScout(request):
    scout = Scout.objects.all()
    serializer = ScoutSerializer(scout, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def addScout(request):
    serializer = ScoutSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['PUT'])
def editScout(request, pk):
    try:
        task = Scout.objects.get(pk=pk)
    except Scout.DoesNotExist:
        return Response(status=404)
    serializer = ScoutSerializer(task, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)

@api_view(['DELETE'])
def deleteScout(request, pk):
    try:
        task = Scout.objects.get(pk=pk)
    except Scout.DoesNotExist:
        return Response(status=404)
    serializer = ScoutSerializer(task)
    task.delete()
    return Response(serializer.data)

# REST FOR PATROL
@api_view(['GET'])
def getAllPatrols(request):
    patrol = Patrol.objects.all()
    serializer = PatrolSerializer(patrol, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def addPatrol(request):
    serializer = PatrolSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['PUT'])
def editPatrol(request, pk):
    try:
        task = Patrol.objects.get(pk=pk)
    except Patrol.DoesNotExist:
        return Response(status=404)
    serializer = PatrolSerializer(task, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)

@api_view(['DELETE'])
def deletePatrol(request, pk):
    try:
        task = Patrol.objects.get(pk=pk)
    except Patrol.DoesNotExist:
        return Response(status=404)
    serializer = PatrolSerializer(task)
    task.delete()
    return Response(serializer.data)
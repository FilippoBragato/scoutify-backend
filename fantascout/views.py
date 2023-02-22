from django.contrib.auth.decorators import login_required, permission_required
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import FantaTask, ScoutCompleteTask
from .serializer import FantaTaskSerializer, ScoutCompleteTaskSerializer

# REST FOR FANTATASK
@permission_required('fantascout.view_fantatask')
@api_view(['GET'])
@login_required
def getAllFantatask(request):
    fantatasks = FantaTask.objects.order_by("type", "-point")
    serializer = FantaTaskSerializer(fantatasks, many=True)
    return Response(serializer.data)

@api_view(['POST'])
@permission_required('fantascout.add_fantatask')
@login_required
def addFantaTask(request):
    serializer = FantaTaskSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['PUT'])
@permission_required('fantascout.change_fantatask')
@login_required
def editFantaTask(request, pk):
    try:
        task = FantaTask.objects.get(pk=pk)
    except FantaTask.DoesNotExist:
        return Response(status=404)
    serializer = FantaTaskSerializer(task, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)


@api_view(['DELETE'])
@permission_required('fantascout.delete_fantatask')
@login_required
def deleteFantaTask(request, pk):
    try:
        task = FantaTask.objects.get(pk=pk)
    except FantaTask.DoesNotExist:
        return Response(status=404)
    serializer = FantaTaskSerializer(task)
    task.delete()
    return Response(serializer.data)

# REST FOR COMPLETE FANTATASK
@api_view(['GET'])
@login_required
@permission_required('fantascout.view_scoutcompletetask')
def getAllScoutCompleteTask(request):
    fantatasks = ScoutCompleteTask.objects.all()
    serializer = ScoutCompleteTaskSerializer(fantatasks, many=True)
    return Response(serializer.data)

@api_view(['POST'])
@login_required
@permission_required('fantascout.add_scoutcompletetask')
def addScoutCompleteTask(request):
    d = request.data
    if request.user.groups.filter(name='ScoutLeader').exists():
        d["checked"] = True
    else:
        d["checked"] = False
    serializer = ScoutCompleteTaskSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['PUT'])
@login_required
@permission_required('fantascout.change_scoutcompletetask')
def editScoutCompleteTask(request, pk):
    try:
        task = ScoutCompleteTask.objects.get(pk=pk)
    except ScoutCompleteTask.DoesNotExist:
        return Response(status=404)
    serializer = ScoutCompleteTaskSerializer(task, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)

@api_view(['DELETE'])
@login_required
@permission_required('fantascout.delete_scoutcompletetask')
def deleteScoutCompleteTask(request, pk):
    try:
        task = ScoutCompleteTask.objects.get(pk=pk)
    except ScoutCompleteTask.DoesNotExist:
        return Response(status=404)
    serializer = ScoutCompleteTaskSerializer(task)
    task.delete()
    return Response(serializer.data)
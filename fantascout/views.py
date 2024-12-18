from django.contrib.auth.decorators import login_required, permission_required
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import FantaTask, ScoutCompleteTask
from .serializer import FantaTaskSerializer, ScoutCompleteTaskSerializer, JoinScoutCompleteTaskSerializer, LadderSerializer
from django.db.models import Sum

# REST FOR FANTATASK
@api_view(['GET'])
def getAllFantatask(request):
    fantatasks = FantaTask.objects.order_by("type", "-point")
    serializer = FantaTaskSerializer(fantatasks, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def addFantaTask(request):
    if request.user.is_authenticated:
        if request.user.has_perm('fantascout.add_fantatask'):
            serializer = FantaTaskSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
            return Response(serializer.data)
        else:
            return Response({'error': 'You should not be here'}, status=401)
    else:
        return Response({'error': 'You should not be here'}, status=401)


@api_view(['PUT'])
def editFantaTask(request, pk):
    if request.user.is_authenticated:
        if request.user.has_perm('fantascout.change_fantatask'):
            try:
                task = FantaTask.objects.get(pk=pk)
            except FantaTask.DoesNotExist:
                return Response(status=404)
            serializer = FantaTaskSerializer(task, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=400)
    return Response({'error': 'You should not be here'}, status=401)


@api_view(['DELETE'])
def deleteFantaTask(request, pk):
    if request.user.is_authenticated:
        if request.user.has_perm('fantascout.delete_fantatask'):
            try:
                task = FantaTask.objects.get(pk=pk)
            except FantaTask.DoesNotExist:
                return Response(status=404)
            serializer = FantaTaskSerializer(task)
            task.delete()
            return Response(serializer.data)
    return Response({'error': 'You should not be here'}, status=401)


# REST FOR COMPLETE FANTATASK
@api_view(['GET'])
def getAllScoutCompleteTask(request):
    if request.user.is_authenticated:
        if request.user.has_perm('fantascout.view_scoutcompletetask'):
            fantatasks = ScoutCompleteTask.objects.all()
            serializer = ScoutCompleteTaskSerializer(fantatasks, many=True)
            return Response(serializer.data)
    return Response({'error': 'You should not be here'}, status=401)

@api_view(['GET'])
def getScoutCompleteTaskToValidate(request):
    if request.user.is_authenticated:
        if request.user.has_perm('fantascout.view_scoutcompletetask'):
            fantatasks = ScoutCompleteTask.objects.select_related("task", "scout", "scout__patrol").filter(checked=False)
            serializer = JoinScoutCompleteTaskSerializer(fantatasks, many=True)
            return Response(serializer.data)
        else:
            return Response({'error': 'You should not be here'}, status=401)
    else:
        return Response({'error': 'You should not be here'}, status=401)

@api_view(['GET'])
def getLadder(request):
    fantatasks = ScoutCompleteTask.objects.select_related("task", "scout", "scout__patrol").filter(checked=True).values('scout__patrol__name').annotate(sum=Sum('task__point')).order_by("-sum")
    serializer = LadderSerializer(fantatasks, many=True)
    return Response(serializer.data, status=200)

@api_view(['GET'])
def getHistory(request):
    fantatasks = ScoutCompleteTask.objects.select_related("task", "scout", "scout__patrol").filter(checked=True).order_by("-date")
    serializer = JoinScoutCompleteTaskSerializer(fantatasks, many=True)
    return Response(serializer.data, status=200)

@api_view(['POST'])
def addScoutCompleteTask(request):
    if request.user.is_authenticated:
        if request.user.has_perm('fantascout.add_scoutcompletetask'):
            d = request.data
            if request.user.groups.filter(name='Leader').exists():
                d["checked"] = True
            else:
                d["checked"] = False
            serializer = ScoutCompleteTaskSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
            return Response(serializer.data)
    return Response({'error': 'You should not be here'}, status=401)

@api_view(['PUT'])
def editScoutCompleteTask(request, pk):
    if request.user.is_authenticated:
        if request.user.has_perm('fantascout.change_scoutcompletetask'):
            try:
                task = ScoutCompleteTask.objects.get(pk=pk)
            except ScoutCompleteTask.DoesNotExist:
                return Response(status=404)
            serializer = ScoutCompleteTaskSerializer(task, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=400)
    return Response({'error': 'You should not be here'}, status=401)


@api_view(['DELETE'])
def deleteScoutCompleteTask(request, pk):
    if request.user.is_authenticated:
        if request.user.has_perm('fantascout.delete_scoutcompletetask'):
            try:
                task = ScoutCompleteTask.objects.get(pk=pk)
            except ScoutCompleteTask.DoesNotExist:
                return Response(status=404)
            serializer = ScoutCompleteTaskSerializer(task)
            task.delete()
            return Response(serializer.data)
    return Response({'error': 'You should not be here'}, status=401)
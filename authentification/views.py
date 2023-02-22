from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from rest_framework.decorators import api_view
from django.contrib.auth.models import Group, User
from .serializer import GroupSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status

# Create your views here.

@api_view(['GET'])
@login_required
def getAllGroups(request):
    groups = Group.objects.filter(user=request.user.id)
    serializer = GroupSerializer(groups, many=True)
    return Response(serializer.data)

class LogoutView(APIView):
    permission_classes = (IsAuthenticated,)
    def post(self, request):
          
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)
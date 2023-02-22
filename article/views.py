from django.contrib.auth.decorators import login_required, permission_required
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Article
from .serializer import ArticleSerializer

# Create your views here.
# REST FOR Article
# @login_required
# @permission_required('fantascout.view_Article')
@api_view(['GET'])
def getAllArticles(request):
    articles = Article.objects.order_by("-date")
    serializer = ArticleSerializer(articles, many=True)
    return Response(serializer.data)

@api_view(['POST'])
# @login_required
# @permission_required('fantascout.add_Article')
def addArticle(request):
    serializer = ArticleSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['PUT'])
# @login_required
# @permission_required('fantascout.change_Article')
def editArticle(request, pk):
    try:
        task = Article.objects.get(pk=pk)
    except Article.DoesNotExist:
        return Response(status=404)
    serializer = ArticleSerializer(task, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)


@api_view(['DELETE'])
# @login_required
# @permission_required('fantascout.delete_Article')
def deleteArticle(request, pk):
    try:
        task = Article.objects.get(pk=pk)
    except Article.DoesNotExist:
        return Response(status=404)
    serializer = ArticleSerializer(task)
    task.delete()
    return Response(serializer.data)

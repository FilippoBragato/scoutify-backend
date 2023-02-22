from django.contrib.auth.decorators import login_required, permission_required
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Article
from .serializer import ArticleSerializer

# REST FOR Article
@api_view(['GET'])
def getAllArticles(request):
    articles = Article.objects.order_by("-date")
    serializer = ArticleSerializer(articles, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def addArticle(request):
    if request.user.is_authenticated:
        if request.user.has_perm('article.add_article'):
            serializer = ArticleSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
            return Response(serializer.data)
    return Response({'error': 'You should not be here'}, status=401)

@api_view(['PUT'])
def editArticle(request, pk):
    if request.user.is_authenticated:
        if request.user.has_perm('article.change_article'):
            try:
                task = Article.objects.get(pk=pk)
            except Article.DoesNotExist:
                return Response(status=404)
            serializer = ArticleSerializer(task, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=400)
    return Response({'error': 'You should not be here'}, status=401)


@api_view(['DELETE'])
def deleteArticle(request, pk):
    if request.user.is_authenticated:
        if request.user.has_perm('article.delete_article'):
            try:
                task = Article.objects.get(pk=pk)
            except Article.DoesNotExist:
                return Response(status=404)
            serializer = ArticleSerializer(task)
            task.delete()
            return Response(serializer.data)
    return Response({'error': 'You should not be here'}, status=401)

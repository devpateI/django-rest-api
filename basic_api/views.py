# from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# from rest_framework.parsers import JSONParser
from .models import Article
from .serializers import ArticleSerializer
from rest_framework import status
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import mixins
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
# Create your views here.

#Generic View 
class GenericArticleAPIView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)

class GenericDetailApiView(generics.GenericAPIView, mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()
    lookup_field = 'id'
    # authentication_classes = [SessionAuthentication, BasicAuthentication] #for basic Authentication
    authentication_classes = [TokenAuthentication] #for Token authentication_classes
    permission_classes = [IsAuthenticated]
    def get(self, request, id=None ):
        return self.retrieve(request)

    def put(self, request , id= None):
        return self.update(request, id)
    
    def delete(self, request, id):
        return self.delete(request,id)
    

# Class based API VIews.
class ArticleAPIView(APIView):
    def get(self, request):
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)
    
    def post(Self, request):
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ArticleDetail(APIView):
    def get_object(self,pk):
        try:
            return Article.objects.get(id=pk)
        except Article.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk, format=None):
        article = self.get_object(pk)
        serializer = ArticleSerializer(article)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        article = self.get_object(pk)
        serializer = ArticleSerializer(article, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        article = self.get_object(pk)
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    #****************************************************************************************************    

# @csrf_exempt #only for basic api
# @api_view(['GET', 'POST'])
# def article_list(request, format = None):
#     """
#     List all code articles, or create a new article.
#     """
    # if request.method == 'GET':
    #     articles = Article.objects.all()
    #     serializer = ArticleSerializer(articles, many=True)
    #     return JsonResponse(serializer.data, safe=False)

    # elif request.method == 'POST':
    #     data = JSONParser().parse(request)
    #     serializer = ArticleSerializer(data=data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return JsonResponse(serializer.data, status=201)
    #     return JsonResponse(serializer.errors, status=400)

    #****************************************************************************************************

    # for Using Django API view
    # if request.method == 'GET':
    #     articles = Article.objects.all()
    #     serializer = ArticleSerializer(articles, many=True)
    #     return Response(serializer.data)

    # elif request.method == 'POST':
    #     serializer = ArticleSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    #****************************************************************************************************

# @csrf_exempt #only for basic api
# @api_view(['GET', 'PUT', 'DELETE'])
# def article_detail(request, pk, format = None):
#     """
#     Retrieve, update or delete a code article.
#     """
    # try:
    #     article = Article.objects.get(pk=pk)
    # except Article.DoesNotExist:
    #     return HttpResponse(status=404)

    # if request.method == 'GET':
    #     serializer = ArticleSerializer(article)
    #     return JsonResponse(serializer.data)

    # elif request.method == 'PUT':
    #     data = JSONParser().parse(request)
    #     serializer = ArticleSerializer(article, data=data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return JsonResponse(serializer.data)
    #     return JsonResponse(serializer.errors, status=400)

    # elif request.method == 'DELETE':
    #     article.delete()
    #     return HttpResponse(status=204)

    #****************************************************************************************************


    # For API View
    # try:
    #     article = Article.objects.get(pk=pk)
    # except Article.DoesNotExist:
    #     return Response(status=status.HTTP_404_NOT_FOUND)

    # if request.method == 'GET':
    #     serializer = ArticleSerializer(article)
    #     return Response(serializer.data)

    # elif request.method == 'PUT':
    #     serializer = ArticleSerializer(article, data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # elif request.method == 'DELETE':
    #     article.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)

    #****************************************************************************************************
    
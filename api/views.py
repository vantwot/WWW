from .serializers import PostSerializer
from django.shortcuts import render
from django.http.response import Http404
from .models import Post
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
# Create your views here.


class PostView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def get_object(self, pk):
        try:
            return Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            raise Http404

    def get(self, request, pk=None, format=None):
        if pk:
            data = self.get_object(pk)
            serializer = PostSerializer(data)
            return Response(serializer.data)      
        else:
            data = Post.objects.all()
            serializer = PostSerializer(data, many=True)
            return Response(serializer.data)

    def post(self, request, format=None):
        data = request.data
        serializer = PostSerializer(data=data)

        serializer.is_valid(raise_exception=True)

        serializer.save()

        response = Response()

        response.data = {
            'message': 'Todo Created Successfully',
            'data': serializer.data
        }

        return response

    def put(self, request, pk=None, format=None):
        todo_to_update = Post.objects.get(pk=pk)
        serializer = PostSerializer(instance=todo_to_update,data=request.data, partial=True)

        serializer.is_valid(raise_exception=True)

        serializer.save()

        response = Response()

        response.data = {
            'message': 'Todo Updated Successfully',
            'data': serializer.data
        }

        return response

    def delete(self, request, pk, format=None):
        todo_to_delete = Post.objects.get(pk=pk)

        # delete the todo
        todo_to_delete.delete()

        return Response({
            'message': 'Todo Deleted Successfully'
        })

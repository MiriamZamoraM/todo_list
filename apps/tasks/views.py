from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Task
from .serializers import TaskSerializer

# Create your views here.

class TaskReg(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

class Retrieve(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        tasks = Task.objects.all().filter(status_delete=False)
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data, status.HTTP_200_OK)


class Update(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request, id):
        task = get_object_or_404(Task, id=id, status_delete=False)
        serializer = TaskSerializer(task, many=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_200_OK)
    

class Delete(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, id):
        task = get_object_or_404(Task, id=id, status_delete=False)
        task.status_delete = True
        task.save()
        return Response({'message':'Eliminado'}, status=status.HTTP_204_NO_CONTENT)
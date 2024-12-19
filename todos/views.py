from rest_framework import generics
from .models import Todo
from .serializers import TodoSerializer

class ListCreateTodoView(generics.ListCreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

class DetailTodoView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
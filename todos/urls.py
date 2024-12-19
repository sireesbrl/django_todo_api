from django.urls import path
from .views import ListCreateTodoView, DetailTodoView

urlpatterns = [
    path("<int:pk>/", DetailTodoView.as_view(), name="todo_detail"),
    path("", ListCreateTodoView.as_view(), name="todo_list"),
]

from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status

from .models import Todo

class TodoModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.todo = Todo.objects.create(title="Test Todo", body="Test Body")
    
    def test_model_content(self):
        self.assertEqual(self.todo.title, "Test Todo")
        self.assertEqual(self.todo.body, "Test Body")
        self.assertEqual(str(self.todo), "Test Todo")
        self.assertEqual(self.todo.status, "Draft")

    def test_api_list_create_view(self):
        response = self.client.get(reverse("todo_list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["title"], "Test Todo")
        self.assertEqual(response.data[0]["body"], "Test Body")
        self.assertEqual(response.data[0]["status"], "Draft")

        response = self.client.post(reverse("todo_list"), data={"title": "Test Todo", "body": "Test Body"})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["title"], "Test Todo")
        self.assertEqual(response.data["body"], "Test Body")
        self.assertEqual(response.data["status"], "Draft")

        response = self.client.get(reverse("todo_list"))
        self.assertEqual(len(response.data), 2)

    def test_api_detail_view(self):
        response = self.client.get(
            reverse("todo_detail", kwargs={"pk": self.todo.id}),
            format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Todo.objects.count(), 1)
        

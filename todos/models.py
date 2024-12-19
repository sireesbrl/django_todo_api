from django.db import models

class Todo(models.Model):
    STATUS_CHOICES = [
        ("completed", "Completed"),
        ("in_progress", "In Progress"),
        ("draft", "Draft"),
    ]
    title = models.CharField(max_length=200)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="Draft")

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-created_at", "-updated_at"]

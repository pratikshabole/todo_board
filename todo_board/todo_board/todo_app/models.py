from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class List(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['title']

class Task(models.Model):
    list = models.ForeignKey(List, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500, null=True, blank=True)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    

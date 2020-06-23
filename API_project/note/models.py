from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

# Create your models here.

class NoteModel(models.Model):
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    title = models.CharField(max_length=64, null=True)
    date = models.DateField(auto_now_add=True)
    body = models.TextField()
    updated_date = models.DateField(auto_now=True)

    def __str__(self):
        return f"{self.title}"

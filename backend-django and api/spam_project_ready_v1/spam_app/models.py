# models.py file content will go here
from django.db import models

class ClassifiedMessage(models.Model):
    message = models.TextField()
    label = models.CharField(max_length=10)  # spam or ham

    def __str__(self):
        return f'{self.label}: {self.message[:50]}'
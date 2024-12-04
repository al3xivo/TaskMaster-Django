from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    due_date = models.DateField()
    priority = models.CharField(
        max_length=10,
        choices=[
            ('Baixa', 'Baixa'),
            ('Média', 'Média'),
            ('Alta', 'Alta')
        ]
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks')

    def __str__(self):
        return self.title

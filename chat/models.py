from django.db import models

# Create your models here.

class Message(models.Model):
    sender = models.TextField()
    receiver = models.TextField()
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.message


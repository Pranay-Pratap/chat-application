from django.db import models
from chats.models import Chat
# Create your models here.

class ChatMessage(models.Model):
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE, related_name="messages")
    username = models.CharField(max_length=120)
    text = models.TextField()

    def __str__(self):
        return f"{self.chat.room_name}-{self.username}" 
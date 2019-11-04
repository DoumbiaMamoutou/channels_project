from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Chat(models.Model):
    """Model definition for Chat."""
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='chat_user')
    message = models.TextField()
    status = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)
    # TODO: Define fields here

    class Meta:
        """Meta definition for Chat."""

        verbose_name = 'Chat'
        verbose_name_plural = 'Chats'

    def __str__(self):
        """Unicode representation of Chat."""
        return self.user.username

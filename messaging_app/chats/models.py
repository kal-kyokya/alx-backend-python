from django.db import models
import uuid
from django.contrib.auth.models import AbstractUser


# -----------------------------------------------------
# An Extension of the 'Abstract User' for values not
# defined in the built-in Django 'User' model
# -----------------------------------------------------
class User(AbstractUser):
    """Adds fields to the built-in Django User model
    Inheritance:
    	AbstractUser: Base class containing methods enabling definition & manipulation of User objects
    """

    user_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField()
    username = models.CharField(max_length=25)
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    phone_number = models.CharField(max_length=12)
    password = None

    def __str__(self):
        """Custom representation of instance upon print operation
        """
        return f"This is {self.username} of user_id: {self.user_id}"


# ---------------------------------------------------------
# The Message model containing sender and conversation
# ---------------------------------------------------------
class Message(models.Model):
    """Blueprint for all Message objects
    Inheritance:
    	models.Model: Base class containing methods facilitating definition and manipulation of custom model objects
    """

    message_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    message_body = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE)

    def __str__(self):
        """Expected output upon print operations
        """
        return f"This is message {self.message_id} sent by {self.sender}"


# -------------------------------------------------------
# The Conversation model tracking user interactions
# -------------------------------------------------------
class Conversation(models.Model):
    """Blueprint for all Conversation objects
    Inheritance:
    	models.Model: Base class containing methods facilitating definition and manipulation of custom model objects
    """

    conversation_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    participants = models.ManyToManyField(User, related_name='conversations')

    def __str__(self):
        """Expected output upon print operations
        """
        return f"This is conversation {self.conversation_id}"

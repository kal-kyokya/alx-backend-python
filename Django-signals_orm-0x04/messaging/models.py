from django.db import models
import uuid
from django.contrib.auth.models import AbstractUser
from .managers import UnreadMessagesManager


# -----------------------------------------------------
# An Extension of the 'Abstract User' for values not
# defined in the built-in Django 'User' model
# -----------------------------------------------------
class User(AbstractUser):
    """Adds fields to the built-in Django User model
    Inheritance:
    	AbstractUser: Base class containing methods enabling definition & manipulation of User objects
    """

    email = models.EmailField()
    username = models.CharField(max_length=25)
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    phone_number = models.CharField(max_length=12)

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
    objects = models.Manager() # Default manager
    unread = UnreadMessagesManager() # Custom manager

    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    sender = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name='sent_messages')
    receiver = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name='received_messages')
    conversation = models.ForeignKey(
        Conversation, on_delete=models.CASCADE,
        related_name='messages')
    edited = models.BooleanField(default=False)
    edited_at = models.DateTimeField(auto_now=True)
    edited_by = models.ForeignKey(User, on_delete=models.CASCADE)
    parent_message = models.ForeignKey(
        'self', null=True, blank=True,
        on_delete=models.CASCADE,
        related_name='replies')
    read = models.BooleanField(default=False)

    def __str__(self):
        """Expected output upon print operations
        """
        return f"This is message {self.message_id} sent by {self.sender}"


# ---------------------------------------------------------
# The Message History model for old versions of messages
# ---------------------------------------------------------
class MessageHistory(models.Model):
    """Blueprint for all MessageHistory objects
    Inheritance:
    	models.Model: Base class containing methods facilitating definition and manipulation of custom model objects
    """

    old_content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, on_delete=models.CASCADE)
    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE)
    edited_by = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name='editor', verbose_name='Edited By')
    message = models.ForeignKey(Message, on_delete=models.CASCADE,
                                related_name='history_entries'
                                verbose_name='Original Message')

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Message History'
        verbose_name_plural = 'Message History'

    def __str__(self):
        """Expected output upon print operations
        """
        return f"This is old message {self.message_id} sent by {self.sender}"


# ---------------------------------------------------------
# The Notification model for content sent to users
# ---------------------------------------------------------
class Notification(models.Model):
    """Blueprint for all Notification objects
    Inheritance:
    	models.Model: Base class containing methods facilitating definition and manipulation of custom model objects
    """

    detail = models.CharField(max_length=255,
                              verbose_name='Notification detail')
    timestamp = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name='notifications', verbose_name='User')
    message = models.ForeignKey(Message, on_delete=models.SET_NULL,
                                related_name='notifications', null=True,
                                verbose_name='Related Message', blank=True)
    was_read = models.BooleanField(default=False, verbose_name='Was Read')

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Notification'
        verbose_name_plural = 'Notifications'

    def __str__(self):
        """Expected output upon print operations
        """
        status = 'read' if self.was_read else 'unread'
        return f"This is notification {self.detail[:32]} sent to {self.user.username} - Status: {status}"


# -------------------------------------------------------
# The Conversation model tracking user interactions
# -------------------------------------------------------
class Conversation(models.Model):
    """Blueprint for all Conversation objects
    Inheritance:
    	models.Model: Base class containing methods facilitating definition and manipulation of custom model objects
    """

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    participants = models.ManyToManyField(User, related_name='conversations')

    def __str__(self):
        """Expected output upon print operations
        """
        return f"This is conversation {self.conversation_id}"

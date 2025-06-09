from django.db import models


# -----------------------------------------------------
# An Extension of the Abstract user for values not
# defined in the built-in Django 'User' model
# -----------------------------------------------------

class User(models.Model):
    """Blueprint for all User objects
    Inheritance:
    	models.Model: Base class containing methods facilitating definition and manipulation of custom model objects
    """

    user_id = models.UUIDField()
    username = models.CharField(max_length=25)
    firstname = models.CharField(max_length=25)
    lastname = models.CharField(max_length=25)
    email = models.EmailField()


# ---------------------------------------------------------
# The Message model containing sender and conversation
# ---------------------------------------------------------

class message(models.Model):
    """Blueprint for all Message objects
    Inheritance:
    	models.Model: Base class containing methods facilitating definition and manipulation of custom model objects
    """

    message_id = models.UUIDField()
    content = models.TextField()
    created_at = models.DateTimeField()
    sender_id = models.ForeignKey(User, on_delete=models.CASCADE)
    conversation_id = models.ForeignKey(Conversation, on_delete=models.CASCADE)


# -------------------------------------------------------
# The Conversation model tracking user interactions
# -------------------------------------------------------

class Conversation(models.Model):
    """Blueprint for all Conversation objects
    Inheritance:
    	models.Model: Base class containing methods facilitating definition and manipulation of custom model objects
    """

    conversation_id = models.UUIDField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

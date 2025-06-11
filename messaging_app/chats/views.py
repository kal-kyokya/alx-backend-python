from django.shortcuts import render
from rest_framework import viewsets
from .serializers import ConversationSerializer, MessageSerializer


class ConversationViewSet(viewsets.ModelViewSet):
    """A 'viewset' for handling operations for the conversation model
    Inheritance:
    	viewsets.ModelViewSet: Collection of Django predefined CRUD executing methods and required attributes.
    """

    serializer_class = ConversationSerializer


class MessageViewSet(viewsets.ModelViewSet):
    """A 'viewset' for handling operations for the message model
    Inheritance:
    	viewsets.ModelViewSet: Collection of Django predefined CRUD executing methods and required attributes.
    """

    serializer_class = MessageSerializer

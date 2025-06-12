from django.shortcuts import render
from rest_framework import viewsets, permissions
from .serializers import ConversationSerializer, MessageSerializer
from .filters import MessageFilter
from django_filters.rest_framework import DjangoFilterBackend
from .permissions import IsParticipantOfConversation


class ConversationViewSet(viewsets.ModelViewSet):
    """A 'viewset' for handling operations for the conversation model
    Inheritance:
    	viewsets.ModelViewSet: Collection of Django predefined CRUD executing methods and required attributes.
    """

    serializer_class = ConversationSerializer
    authentication_class = [JWTAuthentication]
    permission_classes = [
        permissions.IsAuthenticated,
        IsParticipantOfConversation
    ]

    def get_queryset(self):
        """Ensures a user only sees conversations they are a participant of
        Args:
        	self: An object representation of the class instance
        return:
        	Every conversations the user participate in, or None
        """
        if self.request.user.is_authenticated:
            return self.request.user.conversations.all().distinct()
        return Conversation.objects.none()


class MessageViewSet(viewsets.ModelViewSet):
    """A 'viewset' for handling operations for the message model
    Inheritance:
    	viewsets.ModelViewSet: Collection of Django predefined CRUD executing methods and required attributes.
    """

    serializer_class = MessageSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = MessageFilter

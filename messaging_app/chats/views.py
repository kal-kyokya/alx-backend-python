from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from .serializers import ConversationSerializer, MessageSerializer
from .filters import MessageFilter
from .permissions import IsParticipantOfConversation
from .pagination import CustomPagination
from .models import Message, Conversation


class ConversationViewSet(viewsets.ModelViewSet):
    """A 'viewset' (collection of views) handling the Conversation model
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
        	Every conversations associated with the user, or an empty set
        """
        if self.request.user.is_authenticated:
            return self.request.user.conversations.all().distinct()
        return Conversation.objects.none()

    def perform_create(self, serializer):
        """Add the creating user as a participant if not explicitly provided
        Args:
        	self: A representation of the current class instance
        	serializer: The object handling conversion to/from JSON formats
        Return:
        	None
        """
        participants_from_request = serializer.validated_data.get('participants', [])

        if self.request.user not in participants_from_request:
            participants_from_request.append(self.request.user)

        serializer.save(participants=participants_from_request)


class MessageViewSet(viewsets.ModelViewSet):
    """A 'viewset' for handling operations for the message model
    Inheritance:
    	viewsets.ModelViewSet: Collection of Django predefined CRUD executing methods and required attributes.
    """

    serializer_class = MessageSerializer
    authentication_class = [JWTAuthentication]
    permission_classes = [
        permissions.IsAuthenticated,
        IsSenderOrReadOnly
    ]
    pagination_class = CustomPagination
    filter_backends = [DjangoFilterBackend]
    filterset_class = MessageFilter

    def get_queryset(self):
        """Filter messages to only those within a conversation the current user is part of
        Args:
        	self: Instanciation of the current class
        Return:
        	A list of messages or a 403 error if user not authenticated
        """
        if not self.request.user.is_authenticated:
            return Response(status=status.HTTP_403_FORBIDDEN)

        conversation_pk = self.kwargs.get('conversation_pk')
        if not conversation_pk:
            user_conversations = self.request.user.conversation.all()
            return Message.objects.filter(
                conversation__in=user_conversations
            ).select_related(
                'sender', 'conversation'
            ).order_by(
                'created_at'
            )

        try:
            conversation = Conversation.objects.get(
                conversation_id=conversation_pk,
                participants=self.request.user
            )
        except Conversation.DoesNotExist:
            raise status.HTTP_404_NOT_FOUND('Conversation not found or you are not a participant.')

        return Message.objects.filter(
            conversation=conversation
        ).select_related(
            'sender', 'conversation'
        ).order_by(
            'created_at'
        )

    def perform_create(self, serializer):
        """Automatically assigns authenticated user as sender
        Args:
        	self: A representation of the current class instance
        	serializer: The object handling conversion to/from JSON formats
        Return:
        	None
        """
        conversation_pk = self.kwargs.get('conversation_pk')
        if not conversation_pk:
            raise serializers.ValidationError(
                {'conversation_pk': 'Conversation ID must be provided in the URL path.'}
            )
        try:
            # Verify user is a participant of the conversation
            conversation = Conversation.objects.get(
                conversation_id=conversation_pk,
                participants=self.request.user
            )
        except Conversation.DoesNotExist:
            raise permissions.PermissionDenied(
                {'Invalid Conversation ID or you are not a participant of this conversation'}
            )

        serializer.save(
            sender=self.request.user,
            conversation=conversation
        )

    def perform_update(self, serializer):
        """Ensures only the sender can update their message
        Args:
        	self: A representation of the current class instance
        	serializer: The object handling conversion to/from JSON formats
        Return:
        	None if all is good, raises permissions Error otherwise
        """
        if serializer.instance.sender != self.request.user:
            raise permissions.PermissionDenied('You cannot update messages sent by others')

        # Prevent users from changing the sender or conversation of existing messages
        if 'conversation' in serializer.validated_data and \
           serializer.validated_data['conversation'] != serializer.instance.conversation:
            raise permissions.PermissionDenied('You cannot change the conversation of a message.')

        if 'conversation' in serializer.validated_data and\
           serializer.validated_data['sender'] != serializer.instance.sender:
            raise permissions.PermissionDenied('You cannot change the sender of a message.')

        serializer.save()

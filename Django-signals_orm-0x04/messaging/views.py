from rest_framweork import generics
from .models import Message
from django.http import HttpResponse
from django.contrib.decorators import login_required
from django.contrib.auth import logout # Remove the authenticated user's ID from the request and flush their session data


@login_required
def delete_user(request):
    """Ensures a user's details are erased upon logging out
    Args:
    	request: The request object submitted for logout
    Return:
    	An Http response detailing the outcome of the logout attempt
    """
    if request.method == 'DELETE':
        user = request.user
        logout(request)
        user.delete()
        return HttpResponse('User deleted successfully')
    else:
        return HttpResponse('Method not allowed')

class ConversationDetailView(generics.RetrieveAPIView):
    queryset = Conversation.objects.all()
    serializer_class = ConversationSerializer
    permission_classes = [IsAuthenticated]

    def retrieve(self, request, *args, **kwargs):
        conversation_id = kwargs.get('pk')

        # ✅ Optimize: Use prefetch_related and select_related
        conversation = (
            Conversation.objects
            .prefetch_related(
                Prefetch(
                    'messages',
                    queryset=Message.objects.filter(parent_message__isnull=True)
                    .select_related('sender')
                    .prefetch_related('replies')
                ),
                'participants'
            )
            .get(id=conversation_id)
        )

        # ✅ Recursively build threaded messages
        def build_thread(message):
            return {
                'id': message.id,
                'sender': message.sender.username,
                'content': message.content,
                'timestamp': message.timestamp,
                'replies': [build_thread(reply) for reply in message.replies.all()]
            }

        threaded_messages = []
        for message in conversation.messages.all():
            threaded_messages.append(build_thread(message))

        return Response({
            'id': conversation.id,
            'participants': [{'id': user.id, 'username': user.username} for user in conversation.participants.all()],
            'created_at': conversation.created_at,
            'messages': threaded_messages
        })

class MessageCreateView(generics.CreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        data = request.data
        conversation_id = data.get('conversation')
        content = data.get('content')
        parent_message_id = data.get('parent_message')

        if not conversation_id or not content:
            return Response({'error': 'Conversation and content are required.'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            conversation = Conversation.objects.get(id=conversation_id)
        except Conversation.DoesNotExist:
            return Response({'error': 'Conversation not found.'}, status=status.HTTP_404_NOT_FOUND)

        "Test out receiver placement"
        parent_message = None
        if parent_message_id:
            try:
                parent_message = Message.objects.get(id=parent_message_id, conversation=conversation)
            except Message.DoesNotExist:
                return Response({'error': 'Parent message not found in this conversation.'}, status=status.HTTP_404_NOT_FOUND)

        # ✅ Compliant: sender = request.user
        message = Message.objects.create(
            sender=request.user,
            conversation=conversation,
            content=content,
            parent_message=parent_message
        )

        serializer = self.get_serializer(message)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class UnreadMessagesView(generics.ListAPIView):
    """Handles unread messages
    """
    serializer_class = MessageSerializer
    permissions_classes = [IsAuthenticated]

    def get_queryset(self):
        return Message.unread.for_user(self.request.user)


class MarkMessageReadView(generics.UpdateAPIView):
    """Ensures messages are marked as read upon opening
    """
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permissions_classes = [IsAuthenticated]

    def update(self, request, *args, **kwargs):
        message = self.get_object()

        if request.user not in message.conversation.participants.all():
            return Response({'error': 'Permission dnied.'},
                            status=status.HTTP_403_FORBIDDEN)

        message.read = True
        message.save()

        return Response({'message': 'Message marked as read.'})

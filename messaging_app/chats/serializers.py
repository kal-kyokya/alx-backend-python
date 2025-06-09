from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    """Enable User model's 'translation' of JSON data to/from APIs
    Inheritance:
    	serializers.ModelSerializer: Hold required method for actual serialization
    """

    model = User
    fields = (
        'user_id', 'email',
        'username', 'first_name',
        'last_name', 'phone_number'
    )


class MessageSerializer(serializers.ModelSerializer):
    """Enable Message model's 'translation' of JSON data to/from APIs
    Inheritance:
    	serializers.ModelSerializer: Hold required method for actual serialization
    """

    model = Message
    fields = (
        'message_id', 'sent_at',
        'message_body', 'sender',
        'conversation'
    )


class ConversationSerializer(serializers.ModelSerializer):
    """Enable Conversation model's 'translation' of JSON data to/from APIs
    Inheritance:
    	serializers.ModelSerializer: Hold required method for actual serialization
    """

    model = Conversation
    fields = (
        'conversation_id', 'created_at',
        'updated_at', 'participants'
    )

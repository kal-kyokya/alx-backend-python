"""
From the 'serializers module' in the 'rest_framework package' at:
	/django_env/lib/python3.12/site-packages/rest_framework/serializers.py

Serializers and ModelSerializers are similar to Forms and ModelForms.
Unlike forms, they are not constrained to dealing with HTML output, and
form encoded input.

Serialization in REST framework is a two-phase process:

1. Serializers marshal between complex types like model instances, and
python primitives.
2. The process of marshalling between python primitives and request and
response content is handled by parsers and renderers.
"""
from rest_framework import serializers
from .models import User, Message, Conversation


class UserListSerializer(serializers.ModelSerializer):
    """Enable User model's 'translation'  to/from JSON for API communications
    Inheritance:
    	serializers.ModelSerializer: Contains the required methodss for actual serialization
    """
    # For listing/nesting info without sensitive info
    full_name = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = (
            'user_id', 'email',
            'username', 'first_name',
            'last_name', 'phone_number',
            'full_name'
        )

        def get_full_name(self, user_obj):
            """Method shaping 'full_name' when sent client side
            Args:
            	self: Representation of the class instance
            	user_obj: The dict or User Model instance to be processed
            Return:
            	A string representation of the user's full name
            """
            if user_obj.last_name:
                return f"{user_obj.first_name} {user_obj.last_name}"
            else:
                return f"{user_obj.first_name}"

        def validate_phone_number(self, phone_no):
            """Method checking compliance of input attribute to internal rule
            Args:
            	self: An instanciation of 'UserListSerializer'
            	phone_no: The input phone meant to be assessed
            Return:
            	Raises a 'serializers.ValidationError' if input violates the rule, 'phone_no' otherwise
            """
            if not phone_value.startswith('+'):
                raise serializers.ValidationError(
                    "Kindly: Phone number must start with a '+' sign"
                )
            return phone_no

class MessageSerializer(serializers.ModelSerializer):
    """Enable Message model's 'translation' of JSON data to/from APIs
    Inheritance:
    	serializers.ModelSerializer: Contains the required methods for actual serialization
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
    	serializers.ModelSerializer: Contains the required methods for actual serialization
    """

    model = Conversation
    fields = (
        'conversation_id', 'created_at',
        'updated_at', 'participants'
    )

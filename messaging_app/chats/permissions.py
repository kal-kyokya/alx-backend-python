from rest_framework import permissions


class IsSenderOrReadOnly(permissions.BasePermission):
    """Only allows participants in a conversation to send, view, update & delete messages.
    Read-only access is allowed for authenticated user.
    Inheritance:
    	permissions.BasePermission: Enable access to authorization-facilitating methods and attributes
    """

    message = "You do not have permission to perform this action"

    def has_object_permission(self, request, view, message_obj):
        """Manages and asserts read and write permissions.
        Args:
        	self: A representation of the class instance
        	request: The object sent by the user as request
        	view: The function operating at the logic layer
        	message_obj: The Message instance sent by a user
        """
        # Reads permissions are allowed to any request
        # GET, HEAD, OPTIONS are allowed
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed to sender of message
        # Can perform POST, PUT, PATCH and DELETE
        return message_obj.sender == request.user


class IsParticipantOfConversation(permissions.BasePermission):
    """Allows only authenticated users to access the api/view and manage conversations
    Inheritance:
    	permissions.BasePermission: Enable access to authorization facilitating methods and attributes
    """

    def has_object_permission(self, request, view, conversation_obj):
        """Ensures user is listed as participants of a conversation
        Args:
        	self: A representation of the class instance
        	request: The object sent by the user as request
        	view: The function operating at the logic layer
        	conversation_obj: The conversation instance sent by a user
        """
        return request.user in conversation_obj.participants.all()

    def has_permission(self, request, view):
        """For list view, ensure user is authenticated
        Args:
        	self: A representation of the class instance
        	request: The object sent by the user as request
        	view: The function operating at the logic layer
        """
        return request.user and request.user.is_authenticated

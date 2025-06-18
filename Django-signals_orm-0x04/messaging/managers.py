from django.db import models


class UnreadMessagesManager(models.Manager):
    """Custom manager filtering unread messages for a specific user.
    """

    def for_user(self, user):
        """Return unread messages for the given user.
        """
        return super().get_queryset().filter(
            conversation__participants=user,
            read=False
        ).exclude(sender=user).select_related('sender').only(
            'id', 'sender__username',
            'content', 'timestamp',
            'conversation')

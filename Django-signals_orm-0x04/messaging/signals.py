from django.db.models.signals import post_save
from .models import Message
from django.dispatch import receiver
import logging


# A logger named after the current module
logger = logging.getLogger(__name__)

@receiver(post_save, sender=Message)
def message_post_save_handler(sender, instance, created, **kwargs):
    """Triggers a notification on instanciation of 'Message'.
    Args:
    	sender: The model from which the signal is emitted
    	instance: The Message object created before signal emission
    	created: A boolean denoted successful creation of 'instance'
    	**kwargs: Arbitrary keyword arguments passed to the function
    Return:
    	None
    """
    if created:
        try:
            Notification.objects.create(message="You have a new message")

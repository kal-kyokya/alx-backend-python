from django.db.models.signals import post_save
from .models import Message
from django.dispatch import receiver
import logging
from django.db import transaction


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
            Notification.objects.create(
                detail="You have a new message",
                user=instance.receiver,
                message.instance)
            print(f"Notification for {instance.receiver.username} due to message from {instance.sender.username} - ID: {instance.id}")
        except Exception as err:
            print(f"Error creating notification for message ID: {instance.id} - {err}")

@receiver(pre_save, sender=Message)
def log_message_edit(sender, instance, **kwargs):
    """Signal for logging message edits before message is saved
    Args:
    	sender: The model from which the signal is emitted
    	instance: The Message object created before signal emission
    	**kwargs: Arbitrary keyword arguments passed to the function
    Return:
    	None
    """
    # Ensure the message already exists, not being created
    if instance.pk:
        try:
            old_message = sender.objects.get(pk=instance.pk)

            if old_message.content != instance.content:
                with transaction.atomic():
                    MessageHistory.objects.create(
                        message=old_message,
                        edited_by=old_message.sender,
                        old_content=old_message.content)
                    instance.edited = True
                    logger.info(
                        f"Message ID: '{instance.id}' content changed"
                        f"Old content logged to history. New content {instance.content[:50]}")
            else:
                logger.info(f"Message ID: '{instance.id}' saved, but content did not change. No history logged ")
        except sender.DoesNotExist:
            logger.warning(f"Message with ID '{instance.pk}' not found for history logging during pre_save. Was it deleted?")
        except Exception as err:
            logger.error(f"Error logging edit details for message ID: '{instance.id}' - {err}")
    else:
        logger.info(f"New message (ID will be {instance.pk if instance.pk else 'unknown'}) being created. No history logged yet.")

@receiver(post_delete, sender=User)
def deleted_user_signal(sender, instance, **kwargs):
    """Automatically clean up related data when a user deletes their account
    Args:
    	sender: The model from which the signal is emitted
    	instance: The Message object created before signal emission
    	**kwargs: Arbitrary keyword arguments passed to the function
    Return:
    	None
    """
    if instance:
        logger.error(f"Deletion of user with ID: '{instance.id}' was not successful")
    else:
        user_messages = Message.objects.filter(sender=sender)
        user_messages.delete()
        logger.warning(f"User with ID '{sender.id}' has been deleted")

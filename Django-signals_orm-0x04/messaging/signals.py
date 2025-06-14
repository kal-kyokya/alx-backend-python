from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from .models import Message, MessageHistory, Notification


@receiver(post_save, sender=Message)
def message_post_save_handler(sender, instance, created, *args, **kwargs):
    if created:
        Notification.objects.create(message="There is a new message")

@receiver(pre_save, sender=Message)
def message_pre_save_handler(sender, instance, *args, **kwargs):
    MessageHistory.objects.create(**instance)

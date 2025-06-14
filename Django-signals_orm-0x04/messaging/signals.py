from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Message, Notification


@receiver(post_save, sender=Message)
def message_post_save_handler(sender, instance, created, *args, **kwargs):
    if created:
        Notification.objects.create(message="There is a new message")

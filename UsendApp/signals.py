from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Profile

@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        # Only create a profile if one doesn't already exist
        if not hasattr(instance, 'profile'):
            Profile.objects.create(user=instance)
    else:
        instance.profile.save()

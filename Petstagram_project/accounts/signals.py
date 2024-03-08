from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver

from Petstagram_project.accounts.models import Profile

UserModel = get_user_model()


@receiver(post_save, sender=UserModel)
def user_created(sender, instance, created, **kwargs):
    # when create user -> created=True
    # when update user -> created=False
    if not created:
        return

    # Profile.objects.create(user=instance)
    # or:
    profile = Profile(user=instance)
    profile.save()
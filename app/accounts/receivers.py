from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver

from accounts.models import User


@receiver(pre_save, sender=User)
def pre_save_user_last_name_change(sender, instance, **kwargs):
    if instance.last_name:
        instance.last_name = instance.last_name.capitalize()


@receiver(pre_save, sender=User)
def pre_save_user_first_name_change(sender, instance, **kwargs):
    if instance.first_name:
        instance.first_name = instance.first_name.capitalize()


# @receiver(post_save, sender=User)
# def post_save_user(sender, instance, **kwargs):
#     print('USER SIGNAL POST SAVE')

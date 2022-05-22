import uuid

from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models
from django.templatetags.static import static


def upload_avatar(instance, filename: str) -> str:
    return f'{instance.id}/avatars/{filename}'


# class CustomUserManager(UserManager):
#     def create_superuser(self, username=None, email=None, password=None, **extra_fields):
#         user = super().create_superuser(username=None, email=None, password=None, **extra_fields)
#         return user


class User(AbstractUser):
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    # objects = CustomUserManager()

    # TODO
    # username = models.CharField(
    #     max_length=150,
    #     null=True,
    #     unique=True,
    # )
    email = models.EmailField('email address', unique=True)
    avatar = models.FileField(upload_to=upload_avatar, default=None, null=True, blank=True)

    def save(self, *args, **kwargs):
        # print('USER MODEL START SAVE METHOD')

        if not self.username:
            self.username = str(uuid.uuid4())

        # if self.last_name:
        #     self.last_name = self.last_name.capitalize()

        # if self.first_name:
        #     self.first_name = self.first_name.capitalize()

        super().save(*args, **kwargs)

        # print('USER MODEL FINISH SAVE METHOD')

    def avatar_url(self):
        if self.avatar:
            return self.avatar.url

        return static('img/anon_user.png')

    def datamigration_example(self):
        return self.get_full_name()

'''
password = hash('admin');
SELECT * FROM user WHERE username = 'admin' AND password = password;
'''

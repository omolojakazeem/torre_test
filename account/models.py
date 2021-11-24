from django.conf import settings
from django.utils import timezone
from cloudinary.models import CloudinaryField
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.utils.crypto import get_random_string
from django.utils.text import slugify

from .customManager import CustomUserManager
PROFICIENCY = (
    ('MASTER', 'MASTER'),
    ('PROFICIENT', 'PROFICIENT'),
    ('LEARNING', 'LEARNING'),
    ('LEARN IN FUTURE', 'LEARN IN FUTURE'),
)
now = str(timezone.now())
chars = 'abcdefghijklmnopqrstuvwxyz0123456789'
UID_ENCODER = chars + now


def get_my_uiid(code_length, my_char):
    return get_random_string(code_length, my_char)


class Skill(models.Model):
    """
        This model stores information about the skills of a user.
        It has a many-to-many relationship to the UserModel
    """
    title = models.CharField(max_length=255)
    master = models.BooleanField(default=False)
    learning = models.BooleanField(default=False)
    proficient = models.BooleanField(default=True)
    future = models.BooleanField(default=False)
    skill_slug = models.SlugField(null=True, blank=True)

    def save(self, *args, **kwargs):
        self.skill_slug = slugify(self.title)
        super(Skill, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.title}"


class UserModel(AbstractBaseUser, PermissionsMixin):
    """
        This is the User model. Stores:
        - Unique information about a user like:
            - id / pk
            - uiid
            - email
        - Other information like Firstname, Last_name, middlename etc
    """
    uiid = models.CharField(max_length=500, editable=False, blank=True, null=True)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=25, null=True, blank=True)
    last_name = models.CharField(max_length=25, null=True, blank=True)
    middle_name = models.CharField(max_length=25, null=True, blank=True)
    current_role = models.CharField(max_length=25, default="Software Developer")
    image = CloudinaryField()
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    skills = models.ManyToManyField(Skill)
    objects = CustomUserManager()


    USERNAME_FIELD = 'email'

    def save(self, *args, **kwargs):
        self.uiid = get_my_uiid(32, UID_ENCODER)
        super(UserModel, self).save(*args, **kwargs)

    def get_image_url(self):
        return '{}{}'.format(settings.CLOUDINARY_ROOT_URL, self.image)

    @property
    def get_full_name(self):

        if self.first_name is not None and self.last_name is not None:
            return str(self.first_name) + ' ' + str(self.last_name)
        elif self.first_name is None and self.last_name is not None:
            return str(self.last_name)
        elif self.first_name is not None and self.last_name is None:
            return str(self.first_name)
        else:
            return str(self.email) + " (Name not set)"

from django.db  import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    """
    custom user model
    add AUTH_USER_MODEL = 'accounts.User' to settings
    
    first_name, last_name, password, username, is_staff
    """

    email = models.EmailField()

    def __str__(self):
        return self.username



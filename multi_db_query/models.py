from django.db import models


class Users(models.Model):
    """
    I decided create a new model without extending the AbstractUser class because I
    think that the propose of this is a test basically so I keep it simple.

    Note: I know is a better idea to extend the AbstractUser class and add the new fields
    to have the benefits of the Django authentication system and more.
    """

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()

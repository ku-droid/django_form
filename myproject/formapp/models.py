from django.db import models

class Member(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(default='')  # Adding a default value for the email field
    birthdate = models.DateField(null=True, blank=True, default=None)  # Setting default to None
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default='')

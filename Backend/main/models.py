from django.db import models
from django.contrib.auth.models import AbstractUser

from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    number = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    
    class Meta:
        abstract = True

class Artist(User):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    education = models.CharField(max_length=255)
    pseudonym = models.CharField(max_length=100)
    working_experience = models.IntegerField(default=0)
    
    # Add related_name to avoid clashes with auth.User model
    groups = models.ManyToManyField(
        'auth.Group', 
        related_name='artist_groups', 
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='artist_user_permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )

class Client(User):
    basket = models.ManyToManyField('Painting', through='BasketItem')
    address = models.CharField(max_length=255)
    
    # Add related_name to avoid clashes with auth.User model
    groups = models.ManyToManyField(
        'auth.Group', 
        related_name='client_groups', 
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='client_user_permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )

class Painting(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name='paintings')
    name = models.CharField(max_length=255)
    date = models.DateField()
    detail = models.TextField()
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    photo = models.ImageField(upload_to='paintings/')

class BasketItem(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    painting = models.ForeignKey(Painting, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)


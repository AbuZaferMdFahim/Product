from django.db import models
from django.contrib.auth.models import User
from Team.models import Team

# Create your models here.
class Player(models.Model):
    GOALKEEPER = 'goalkeeper'
    DEFENDER = 'defender'
    MIDFIELDER = 'midfielder'
    FORWARD = 'forward'

    POSITION_CHOICES = [
        (GOALKEEPER, 'Goalkeeper'),
        (DEFENDER, 'Defender'),
        (MIDFIELDER, 'Midfielder'),
        (FORWARD, 'Forward'),
    ]
    
    RATING_CHOICES = [
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
        (6, '6'),
        (7, '7'),
        (8, '8'),
        (9, '9'),
        (10, '10'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    bio = models.TextField(null=True)
    kit = models.IntegerField(unique=True)
    team = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True, blank=True, related_name='player')
    position = models.CharField(
        max_length=50,
        choices=POSITION_CHOICES,
        default=MIDFIELDER,
    )
    age = models.IntegerField()
    img = models.ImageField(upload_to='player_images/')
    NID_number = models.CharField(max_length=100)
    nationality = models.CharField(max_length=100, null=True)
    nationality_image = models.ImageField(upload_to='player_nationality_images/', null=True)
    rating = models.IntegerField(choices=RATING_CHOICES,default=5)  # Rating field from 1 to 10
    
    def __str__(self):
        return self.name



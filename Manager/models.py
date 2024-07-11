from django.db import models
from django.contrib.auth.models import User
from Team.models import Team

class Manager(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    bio = models.TextField(null=True)
    role = models.CharField(max_length=100, null=True)
    team = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True, blank=True, related_name='manager')
    age = models.IntegerField()
    img = models.ImageField(upload_to='manager_images/')
    NID_number = models.CharField(max_length=100)
    nationality = models.CharField(max_length=100, null=True)
    nationality_image = models.ImageField(upload_to='manager_nationality_images/', null=True)
    
    def __str__(self):
        return self.name

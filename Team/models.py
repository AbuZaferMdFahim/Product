from django.db import models

class Team(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    logo = models.ImageField(upload_to='team_logos/', null=True, blank=True)
    established = models.DateField()
    
    def __str__(self):
        return self.name

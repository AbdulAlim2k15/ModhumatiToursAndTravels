from django.db import models

class PopularLocation(models.Model):
    name = models.CharField(max_length=100, unique=True)  # Name of the location
    description = models.TextField()  # Description of the location
    image = models.ImageField(upload_to='popular_locations/')  # Image of the location
    region = models.CharField(max_length=100, blank=True, null=True)


    def __str__(self):
        return self.name


class TeamMember(models.Model):
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    image = models.ImageField(upload_to='team_members/')  # Stores images in 'media/team_members/'

    def __str__(self):
        return self.name

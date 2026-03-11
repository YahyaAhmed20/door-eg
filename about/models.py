from django.db import models
from cloudinary.models import CloudinaryField


class AboutHeader(models.Model):
    title = models.CharField(max_length=200)
    header_image = CloudinaryField(verbose_name="about/headers/")


    def __str__(self):
        return self.title
    
    
from django.db import models

class AboutSection(models.Model):
    section_title = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    description1 = models.TextField()
    description2 = models.TextField()

    experience_years = models.IntegerField()

    image1 = CloudinaryField(verbose_name='about/')
    image2 = CloudinaryField(verbose_name='about/')


    def __str__(self):
        return self.section_title
    
    
from django.db import models


class FeatureSection(models.Model):
    section_title = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    description = models.TextField()

    image1 = CloudinaryField(verbose_name='features/')
    image2 = CloudinaryField(verbose_name='features/')
    
    


    def __str__(self):
        return self.section_title
    
class Feature(models.Model):
    section = models.ForeignKey(
        FeatureSection,
        on_delete=models.CASCADE,
        related_name='features'
    )

    icon = CloudinaryField(verbose_name='features/icons/')
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title
    
    
from django.db import models

class TeamSection(models.Model):
    section_title = models.CharField(max_length=100)
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.section_title
    
    
class TeamMember(models.Model):
    section = models.ForeignKey(
        TeamSection,
        on_delete=models.CASCADE,
        related_name='members'
    )

    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)

    image = CloudinaryField(verbose_name='team/')

    facebook = models.URLField(blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name
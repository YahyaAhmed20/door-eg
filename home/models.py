from django.db import models
from cloudinary.models import CloudinaryField

class Carousel(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    button_text = models.CharField(max_length=50, default="View Catalog")

    def __str__(self):
        return self.title


class CarouselImage(models.Model):
    carousel = models.ForeignKey(
        Carousel,
        on_delete=models.CASCADE,
        related_name="images"
    )
    image = CloudinaryField(verbose_name="carousel")


    def __str__(self):
        return f"Image for {self.carousel.title}"
    
    
class Fact(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    icon = CloudinaryField(verbose_name="facts/")

    order = models.IntegerField(default=0)

    def __str__(self):
        return self.title
    
class Service(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = CloudinaryField(verbose_name="services/")

    icon = CloudinaryField(verbose_name="services/icons/")

    order = models.IntegerField(default=0)

    def __str__(self):
        return self.title
    
    
class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    
    image = CloudinaryField(verbose_name="projects/")

    order = models.IntegerField(default=0)

    def __str__(self):
        return self.title
    
    
class Testimonial(models.Model):
    name = models.CharField(max_length=200)
    profession = models.CharField(max_length=200)
    message = models.TextField()
    image = CloudinaryField(verbose_name="testimonials/")

    order = models.IntegerField(default=0)

    def __str__(self):
        return self.name
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
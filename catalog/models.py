from django.db import models
class Catalog(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='catalog_images/')
    drive_link = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
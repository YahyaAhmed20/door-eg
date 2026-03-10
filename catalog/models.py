from django.db import models

class Catalog(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='catalog_images/')
    
    pdf = models.FileField(upload_to='catalog_pdfs/', blank=True, null=True)
    drive_link = models.URLField(blank=True, null=True)

    order = models.PositiveIntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['order']

    def get_catalog_url(self):
        if self.pdf:
            return self.pdf.url
        return self.drive_link

    def __str__(self):
        return self.title
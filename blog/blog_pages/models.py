from django.db import models


class page(models.Model):
    title= models.CharField(max_length=30)
    subtitle=models.CharField(max_length=30)
    body=models.CharField(max_length=2000)
    author=models.CharField(max_length=30)
    date=models.DateField()
    image=models.ImageField(null=True, blank=True, upload_to="imagenes/")

    @property
    def image_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url
    
    def __str__(self):
        return f'{self.title}'

from django.db import models

class ImageOfTheDay(models.Model):
    image_url = models.URLField(max_length = 200)
    last_updated = models.DateField(null=True, blank=True)

    class Meta:
        # Especifica el campo para obtener el último registro
            get_latest_by = 'last_updated'
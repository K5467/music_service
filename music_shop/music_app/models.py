from django.db import models

class Song(models.Model):
    title = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    year = models.PositiveIntegerField()
    demo_url = models.URLField()
    full_url = models.URLField(blank=True, null=True)
    is_purchased = models.BooleanField(default=False)

    def __str__(self):
        return self.title
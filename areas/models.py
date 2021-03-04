from django.db import models


class Area(models.Model):

    COLOR = 'CLR'
    GRADIENT = 'GRD'
    TYPE_CHOICES = (
        (COLOR, 'COLOR'),
        (GRADIENT, 'GRADIENT'),
    )

    name = models.CharField(max_length=255)
    description = models.TextField()
    longitude = models.FloatField()
    latitude = models.FloatField()

    fill_type = models.CharField(choices=TYPE_CHOICES, default=COLOR, max_length=10)

    color = models.CharField(max_length=6, help_text='LIKE AA0192', blank=True)
    color1 = models.CharField(max_length=6, help_text='LIKE A90BCA', blank=True)
    color2 = models.CharField(max_length=6, help_text='LIKE FED562', blank=True)
    angle = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f'{self.name.lower()}'

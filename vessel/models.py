from django.db import models


class Vessel(models.Model):

    code = models.CharField('Code', max_length=255, unique=True)

    def __str__(self):
        return self.code

    class Meta:
        verbose_name = 'Vessel'
        verbose_name_plural = 'Vessels'
        ordering = ['id', 'code']

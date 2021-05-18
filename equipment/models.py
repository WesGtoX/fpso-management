from django.db import models
from equipment import COUNTRY_LIST


class Equipment(models.Model):
    name = models.CharField('Name', max_length=255)
    code = models.CharField('Code', max_length=255, unique=True)
    location = models.CharField('Code', choices=COUNTRY_LIST, max_length=255, blank=False, null=False)
    status = models.BooleanField('Status', blank=False, null=False, default=True)

    vessel = models.ForeignKey(
        'vessel.Vessel', blank=False, null=False,
        verbose_name='Vessel', related_name='vessel',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f'{self.name}, {self.code}'

    def _get_location(self):
        country_list = dict(i[::-1] for i in COUNTRY_LIST)
        return country_list.get(self.location)

    class Meta:
        verbose_name = 'Equipment'
        verbose_name_plural = 'Equipment'
        ordering = ['id', 'name']

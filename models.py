from __future__ import unicode_literals, division
from django.utils.encoding import python_2_unicode_compatible
from django.db import models

@python_2_unicode_compatible
class SplDrug(models.Model):
    name = models.CharField(max_length=5000)
    idcode = models.CharField(max_length=100)
    packager = models.CharField(max_length=150, null=True, blank=True)

    def __str__(self):
        return '%s' % self.name    


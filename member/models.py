from __future__ import unicode_literals

from django.utils import timezone
from django.db import models


class Member(models.Model):
    email = models.EmailField()
    when = models.DateTimeField(default=timezone.now)

    def __unicode__(self):
        return self.email

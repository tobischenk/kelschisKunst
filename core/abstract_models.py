from django.db import models
from django.utils import timezone


class TrackCreationAndUpdates(models.Model):
    class Meta:
        abstract = True

    created_at = models.DateTimeField(auto_now_add=True, blank=False, null=False)
    updated_at = models.DateTimeField(auto_now=True, blank=False, null=False)

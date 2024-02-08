from django.db import models
from django.utils import timezone

from core.abstract_models import TrackCreationAndUpdates
from core.models import BaseImage


# Create your models here.
class ShowroomImage(TrackCreationAndUpdates):
    image = models.ForeignKey(BaseImage, on_delete=models.CASCADE)

    # Date when the Image should be published, Used to schedule a Task for when that should be done
    publish_at = models.DateTimeField(null=True, default=(timezone.now() + timezone.timedelta(weeks=1)))
    public = models.BooleanField(default=False, blank=False, null=False)

    def __str__(self):
        return f"Showroom - {self.image}"

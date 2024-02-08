import os

from django.db import models
from django.utils import timezone

from config.settings import BASE_DIR
from core.abstract_models import TrackCreationAndUpdates


# Create your models here.
class ImageMedium(TrackCreationAndUpdates):
    class Meta:
        db_table = "images_medium"
        verbose_name = "Medium"
        verbose_name_plural = "Mediums"

    name = models.CharField(max_length=1024)
    description = models.CharField(max_length=5000, null=False, blank=True)

    def __str__(self):
        return f"Medium - {self.name}"


class BaseImageMedium(TrackCreationAndUpdates):
    class Meta:
        db_table = "images_base_image_medium"
        verbose_name = "Image Medium"

    base_image = models.ForeignKey("core.BaseImage", on_delete=models.CASCADE)
    medium = models.ForeignKey(ImageMedium, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.base_image} - {self.medium}"


class ImagePaintingSurface(TrackCreationAndUpdates):
    class Mate:
        db_table = "images_painting_surface"
        verbose_name = "Painting Surface"
        verbose_name_plural = "Painting Surfaces"

    name = models.CharField(max_length=1024)
    description = models.CharField(max_length=5000, null=False, blank=True)

    def __str__(self):
        return f"PaintingSurface - {self.name}"


class BuyerPersona(TrackCreationAndUpdates):
    class Meta:
        db_table = "images_buyer_persona"
        verbose_name = "Buyer Persona"
    first_name = models.CharField(max_length=1024, null=False, blank=False)
    last_name = models.CharField(max_length=1024, null=False, blank=False)
    email = models.EmailField(null=True, blank=True)

    def __str__(self):
        return f"Buyer - {self.first_name} {self.last_name}"


class BaseImageBuyer(TrackCreationAndUpdates):
    class Meta:
        db_table = "images_image_buyer"
        verbose_name = "Image Buyer"

    image = models.ForeignKey("core.BaseImage", on_delete=models.SET_NULL, null=True)
    buyer_persona = models.ForeignKey(BuyerPersona, on_delete=models.SET_NULL, null=True)
    price = models.DecimalField(null=False, blank=False, decimal_places=2, max_digits=12)
    can_be_named = models.BooleanField(default=False, null=False, blank=False)

    def __str__(self):
        return (
            f"{self.image} - {self.buyer_persona} "
            f"({self.price}, public: {'yes' if self.can_be_named else 'no'})"
        )


class BaseImage(TrackCreationAndUpdates):
    class Meta:
        db_table = "images_base_image"
        verbose_name = "Base Image"
        verbose_name_plural = "Base Images"

    # Foreign Key to ImageUpload
    file = models.ImageField(upload_to="images/")

    #  Title and Description for Image
    title = models.CharField(max_length=1024, blank=False, null=False)
    description = models.TextField(blank=True, null=False)

    # Date related Fields
    started_at = models.DateField(
        null=False, blank=False,
        default=(timezone.now() - timezone.timedelta(weeks=16))
    )
    finished_at = models.DateField(null=False, blank=False, default=timezone.now)

    # Dimensions
    width = models.SmallIntegerField(null=False, blank=False)
    height = models.SmallIntegerField(null=False, blank=False)

    # Medium - What Materials where used to create the image
    medium = models.ManyToManyField(to=ImageMedium, related_name="base_images", through=BaseImageMedium)
    # Malgrund - WHat was the image drawn or created on
    painting_surface = models.ForeignKey(ImagePaintingSurface, on_delete=models.CASCADE)

    # Buying related Information
    available_to_buy = models.BooleanField(default=False, blank=False, null=False)
    price = models.DecimalField(null=True, blank=False, default=500.00, decimal_places=2, max_digits=12)
    transactions = models.ManyToManyField(to=BuyerPersona, through=BaseImageBuyer)

    def __str__(self):
        return f"Image - {self.title}"

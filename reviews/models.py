from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from core import models as core_models


class Review(core_models.TimestampedModel):

    """ Review Model Definition """

    review = models.TextField()
    check_in = models.IntegerField(
        validators=[MaxValueValidator(5), MinValueValidator(1)]
    )
    communication = models.IntegerField(
        validators=[MaxValueValidator(5), MinValueValidator(1)]
    )
    accuracy = models.IntegerField(
        validators=[MaxValueValidator(5), MinValueValidator(1)]
    )
    location = models.IntegerField(
        validators=[MaxValueValidator(5), MinValueValidator(1)]
    )
    cleanliness = models.IntegerField(
        validators=[MaxValueValidator(5), MinValueValidator(1)]
    )
    value = models.IntegerField(validators=[MaxValueValidator(5), MinValueValidator(1)])
    user = models.ForeignKey(
        "users.User", related_name="reviews", on_delete=models.CASCADE
    )
    room = models.ForeignKey(
        "rooms.Room", related_name="reviews", on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.review} - {self.room}"

    def rating_average(self):
        avg = (
            self.accuracy
            + self.communication
            + self.cleanliness
            + self.location
            + self.check_in
            + self.value
        ) / 6
        return round(avg, 2)

    rating_average.short_description = "Avg."

    class Meta:
        ordering = ("-created",)

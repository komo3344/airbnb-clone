from django.db import models
from core import models as core_models


class Review(core_models.TimestampedModel):

    """ Review Model Definition """

    review = models.TextField()
    check_in = models.IntegerField()
    communication = models.IntegerField()
    accuracy = models.IntegerField()
    location = models.IntegerField()
    cleanliness = models.IntegerField()
    value = models.IntegerField()
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
            self.check_in
            + self.communication
            + self.accuracy
            + self.location
            + self.cleanliness
            + self.value
        ) / 6
        return round(avg, 2)

from django.db import models
from django_countries.fields import CountryField
from core import models as core_models


class AbstractItem(core_models.TimestampedModel):

    """ Abstract Item """

    name = models.CharField(max_length=80)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class RoomType(AbstractItem):

    pass

    class Meta:
        verbose_name = "Room type"


class Amenity(AbstractItem):

    pass

    class Meta:
        verbose_name_plural = " Amenities"


class Facility(AbstractItem):

    pass

    class Meta:
        verbose_name_plural = "Facilities"


class HouseRule(AbstractItem):

    pass

    class Meta:
        verbose_name = "House Rule"


class Photo(core_models.TimestampedModel):
    caption = models.CharField(max_length=80)
    file = models.ImageField(null=True, upload_to="room_photos")
    room = models.ForeignKey("ROOM", related_name="photos", on_delete=models.CASCADE)

    def __str__(self):
        return self.caption


class Room(core_models.TimestampedModel):

    """ Room Model Definition """

    name = models.CharField(max_length=140)
    description = models.TextField()
    country = CountryField()
    city = models.CharField(max_length=80)
    price = models.IntegerField()
    address = models.CharField(max_length=140)
    guests = models.IntegerField()
    beds = models.IntegerField()
    bedrooms = models.IntegerField()
    baths = models.IntegerField()
    check_in = models.TimeField()
    check_out = models.TimeField()
    instant_book = models.BooleanField(default=False)  # 즉시 예약
    host = models.ForeignKey(
        "users.User", related_name="rooms", on_delete=models.CASCADE
    )
    # 한사람이 하나의 룸타입만 선택가능하며 룸타입을 제거해도 룸을 제거하지 않음
    room_type = models.ForeignKey(
        "RoomType", related_name="rooms", on_delete=models.SET_NULL, null=True
    )

    amenities = models.ManyToManyField("Amenity", related_name="rooms", blank=True)
    facilities = models.ManyToManyField("Facility", related_name="rooms", blank=True)
    house_rules = models.ManyToManyField("HouseRule", related_name="rooms", blank=True)

    def __str__(self):
        return self.name

    def total_rating(self):
        all_reviews = self.reviews.all()
        all_ratings = 0

        for review in all_reviews:
            if len(all_reviews) > 0:
                all_ratings += review.rating_average()
                return round(all_ratings / len(all_reviews), 2)
            return 0

    total_rating.short_description = "AVG."

    def save(self, *args, **kwargs):
        self.city = str.capitalize(self.city)
        super().save(*args, **kwargs)

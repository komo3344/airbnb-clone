from django.contrib import admin
from . import models


@admin.register(models.Reservation)
class ReservationAdmin(admin.ModelAdmin):

    """ Reservation Admin Definition """

    list_display = (
        "room",
        "check_in",
        "check_out",
        "status",
        "in_progressing",
        "is_finished",
        "guest",
    )


@admin.register(models.BookedDay)
class BookedDayAdmin(admin.ModelAdmin):
    list_display = ("day", "reservation")

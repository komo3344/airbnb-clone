from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models
from rooms import models as rooms_models


class RoomInline(admin.StackedInline):
    model = rooms_models.Room
    extra = 1
    classes = ["collapse"]


@admin.register(models.User)
class CustomUserAdmin(UserAdmin):

    """ Custom User Admin """

    inlines = (RoomInline,)
    fieldsets = UserAdmin.fieldsets + (
        (
            "Custom Profile",
            {
                "fields": (
                    "avatar",
                    "gender",
                    "bio",
                    "birthdate",
                    "language",
                    "currency",
                    "superhost",
                )
            },
        ),
    )

    list_display = ("username", "email", "gender", "language", "currency", "superhost")
    list_filter = UserAdmin.list_filter + ("superhost",)

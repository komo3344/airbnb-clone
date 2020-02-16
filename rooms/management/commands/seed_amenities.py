from django.core.management.base import BaseCommand
from rooms.models import Amenity  # 모델이 하나밖에 없다면 이렇게 써도 무방

# from rooms import models as room_models  why? 이 모델이 어디서 왔는지 알기위해서


class Command(BaseCommand):
    help = "This commend make Amenities"

    # def add_arguments(self, parser):
    #     parser.add_argument(
    #         "--times",
    #         help="How many times do you want to me to tell you that I love you?",
    #     )

    def handle(self, *args, **options):
        amenities = [
            "Kitchen",
            "Shampoo",
            "Heating",
            "Air conditioning",
            "Washer",
            "Dryer",
            "Wifi",
            "Breakfast",
            "Indoor fireplace",
            "Hangers",
            "Iron",
            "Hair dryer",
            "Laptop-friendly workspace",
            "TV",
            "Crib",
            "High chair",
            "Self check-in",
            "Smoke alarm",
            "Carbon monoxide alarm",
            "Private bathroom",
        ]
        for a in amenities:
            Amenity.objects.create(name=a)
        self.stdout.write(self.style.SUCCESS(f'{len(amenities)} Amenities created'))

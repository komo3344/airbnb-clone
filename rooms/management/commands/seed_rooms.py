import random
from django.core.management.base import BaseCommand
from django.contrib.admin.utils import flatten
from django_seed import Seed
from rooms import models as room_models
from users import models as user_models


class Command(BaseCommand):
    help = "This commend make Rooms"

    def add_arguments(self, parser):
        parser.add_argument(
            "--number", help="How many rooms you want to create?", default=1, type=int
        )

    def handle(self, *args, **options):
        number = options.get("number")
        all_users = user_models.User.objects.all()
        all_roomtypes = room_models.RoomType.objects.all()

        seeder = Seed.seeder()
        seeder.add_entity(
            room_models.Room,
            number,
            {
                "host": lambda x: random.choice(all_users),
                "room_type": lambda x: random.choice(all_roomtypes),
                "guests": lambda x: random.randint(1, 20),
                "price": lambda x: random.randint(1, 300),
                "beds": lambda x: random.randint(1, 5),
                "bedrooms": lambda x: random.randint(1, 5),
                "baths": lambda x: random.randint(1, 5),
                "name": lambda x: seeder.faker.address(),
            },
        )
        create_photos = seeder.execute()
        create_clean = flatten(list(create_photos.values()))
        amenities = room_models.Amenity.objects.all()
        facilities = room_models.Facility.objects.all()
        rules = room_models.HouseRule.objects.all()

        for pk in create_clean:
            room = room_models.Room.objects.get(pk=pk)
            for i in range(3, random.randint(10, 30)):
                room_models.Photo.objects.create(
                    caption=seeder.faker.sentence(),
                    file=f"room_photos/{random.randint(1, 31)}.webp",
                    room=room,
                )
            for a in amenities:
                magic_number = random.randint(0, 15)
                if magic_number & 2 == 0:
                    room.amenities.add(a)
            for f in facilities:
                magic_number = random.randint(0, 15)
                if magic_number & 2 == 0:
                    room.facilities.add(f)
            for r in rules:
                magic_number = random.randint(0, 15)
                if magic_number & 2 == 0:
                    room.house_rules.add(r)  # room모델 안의 house_rules /
                    # rules = room_models.HouseRule.objects.all()과 착각 X

        self.stdout.write(self.style.SUCCESS(f"{number} Rooms created"))

from django.core.management.base import BaseCommand
from rooms.models import Facility  # 모델이 하나밖에 없다면 이렇게 써도 무방


class Command(BaseCommand):
    help = "This commend make Amenities"

    # def add_arguments(self, parser):
    #     parser.add_argument(
    #         "--times",
    #         help="How many times do you want to me to tell you that I love you?",
    #     )

    def handle(self, *args, **options):
        facilities = [
            "Free parking on premises",
            "Gym",
            "Hot tub",
            "Pool",
        ]
        for f in facilities:
            Facility.objects.create(name=f)
        self.stdout.write(self.style.SUCCESS(f"{len(facilities)} Facilities created"))

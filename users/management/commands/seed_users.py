from django.core.management.base import BaseCommand
from django_seed import Seed
from users.models import User  # 모델이 하나밖에 없다면 이렇게 써도 무방


class Command(BaseCommand):
    help = "This commend make Users"

    def add_arguments(self, parser):
        parser.add_argument(
            "--number", default="1", help="How many do you create users?", type=int
        )

    def handle(self, *args, **options):
        number = options.get("number", 2)
        seeder = Seed.seeder()
        seeder.add_entity(User, number, {"is_staff": False, "is_superuser": False})
        seeder.execute()
        self.stdout.write(self.style.SUCCESS(f"{number} users created"))

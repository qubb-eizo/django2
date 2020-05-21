from django.core.management.base import BaseCommand

from group.models import Group
from student.models import Student


class Command(BaseCommand):
    help = 'Generate students'

    def add_arguments(self, parser):
        parser.add_argument('count', type=int)

    def handle(self, *args, **kwargs):
        count = kwargs['count']
        Student.objects.all().delete()
        groups = list(Group.objects.all())
        for _ in range(count):
            Student.generate_student(groups)

            self.stdout.write(self.style.SUCCESS(f'Created: {count} students'))

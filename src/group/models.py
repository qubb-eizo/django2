import random
from django.db import models
from faker import Faker
from teacher.models import Teacher


class Classroom(models.Model):
    name = models.CharField(max_length=64)
    floor = models.SmallIntegerField(max_length=128, null=True)

    def __str__(self):
        return f'{self.name} - {self.floor}'

    @classmethod
    def generate_classroom(cls):
        group = cls(
            name=f'Classroom - {random.choice(range(5))}',
            floor=random.choice(range(10))
        )

        group.save()


class Group(models.Model):
    group_name = models.CharField(max_length=40, null=False)
    group_number = models.CharField(max_length=2, null=False)
    teacher = models.ForeignKey(
        to=Teacher, null=True,
        on_delete=models.SET_NULL, db_constraint=True, related_name='groups')
    classroom = models.ManyToManyField(to=Classroom, null=True, related_name='groups')

    def __str__(self):
        return f'{self.group_name}, ' \
               f'{self.group_number}'

    @classmethod
    def generate_group(cls):
        fake = Faker()

        group = cls(
            group_name=fake.last_name(),
            group_number=random.randint(1, 100)
        )

        group.save()

import random

from django.db import models
from faker import Faker


class Group(models.Model):
    group_name = models.CharField(max_length=40, null=False)
    group_number = models.CharField(max_length=2, null=False)

    def __str__(self):
        return f'{self.group_name}, {self.group_number}'

    @classmethod
    def generate_group(cls):
        fake = Faker()

        group = cls(
            group_name=fake.last_name(),
            group_number=random.randint(1, 100)
        )

        group.save()

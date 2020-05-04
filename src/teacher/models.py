
import datetime
from django.db import models
from faker import Faker


class Teacher(models.Model):
    first_name = models.CharField(max_length=40, null=False)
    last_name = models.CharField(max_length=20, null=False)
    email = models.CharField(max_length=50, null=True)
    birthdate = models.DateField(default=datetime.datetime.now())

    def __str__(self):
        return f'{self.first_name}, {self.last_name}, {self.email}'

    @classmethod
    def generate_teacher(cls):
        faker = Faker()

        teacher = cls(
            first_name=faker.first_name(),
            last_name=faker.last_name(),
            email=faker.email()
        )

        teacher.save()

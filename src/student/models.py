import datetime
from django.db import models
from faker import Faker

from group.models import Group


class Student(models.Model):
    first_name = models.CharField(max_length=40, null=False)
    last_name = models.CharField(max_length=20, null=False)
    email = models.EmailField(max_length=50, null=True, unique=True)
    birthdate = models.DateField(default=datetime.date.today)
    phone_number = models.CharField(default=380000000000, max_length=15, unique=True)
    group = models.ForeignKey(to=Group, null=True, on_delete=models.SET_NULL, db_constraint=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['first_name', 'last_name'], name='name of constraint students')
        ]

    def __str__(self):
        return f'{self.first_name}, ' \
               f'{self.last_name}, ' \
               f'{self.email},' \
               f'{self.phone_number},' \
               f'{self.birthdate}'

    @classmethod
    def generate_student(cls):
        faker = Faker(['uk_UA'])

        student = cls(
            first_name=faker.first_name(),
            last_name=faker.last_name(),
            email=faker.email(),
            phone_number=faker.phone_number()
        )

        student.save()

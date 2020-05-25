from django.db import models
from faker import Faker
import datetime


class Teacher(models.Model):
    first_name = models.CharField(max_length=40, null=False)
    last_name = models.CharField(max_length=20, null=False)
    email = models.EmailField(max_length=50, null=True, unique=True)
    birthdate = models.DateField(default=datetime.date.today)
    phone_number = models.CharField(max_length=12, default=380000000000, unique=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['first_name', 'last_name'], name='name of constraint teachers')
        ]

    def full_info(self):
        return f'{self.first_name},  ' \
               f'{self.last_name}, ' \
               f'{self.email}, ' \
               f'{self.phone_number}'

    def __str__(self):
        return self.full_info()

    @classmethod
    def generate_teacher(cls):
        faker = Faker(['uk_UA'])

        teacher = cls(
            first_name=faker.first_name(),
            last_name=faker.last_name(),
            email=faker.email(),
            phone_number=faker.phone_number()
        )

        teacher.save()

from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from PIL import Image
from django.core.files.base import ContentFile
from io import BytesIO


class UserAccountProfile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='profile')
    image = models.ImageField(default='default.jpg', upload_to='pics')

    def save(self, *args, **kwargs):
        bw_image = Image.open(self.image).convert('L')

        new_image_io = BytesIO()
        bw_image.save(new_image_io, format='png')

        self.image.save(name='new_image',
                        content=ContentFile(new_image_io.getvalue()),
                        save=False
                        )

        super().save(*args, **kwargs)

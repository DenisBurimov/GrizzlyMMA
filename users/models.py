from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class UserProfile(models.Model):
    STATUS_CHOISES = (
        ("Undefined", "Undefined"),
        ("Coach", "Coach"),
        ("Manager", "Manager"),
        ("Receptionist", "Receptionist"),
        ("Student", "Student"),
        ("Parent", "Parent"),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=12, default="YourPhone")
    picture = models.ImageField(upload_to="users/", default="default_user.jpg", blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOISES, default="Undefined")

    def __str__(self):
        return f"{self.user}, status: {self.status}"

    # def save(self, *args, **kwargs):
    #     super(UserProfile, self).save(*args, **kwargs)
    #
    #     img = Image.open(self.picture.path)
    #
    #     if img.height > 300 or img.width > 300:
    #         output_size = (300, 300)
    #         img.thumbnail(output_size)
    #         img.save(self.picture.path)
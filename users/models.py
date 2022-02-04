from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    STATUS_CHOISES = (
        ("U", "Undefined"),
        ("C", "Coach"),
        ("M", "Manager"),
        ("R", "Receptionist"),
        ("S", "Student"),
        ("P", "Parent"),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=12, default="YourPhone")
    picture = models.ImageField(upload_to="users/", default="default_user.jpg", blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOISES, default="Undefined")

    def __str__(self):
        return f"{self.user}"

from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.utils import timezone
from django.urls import reverse


class Manager(models.Model):
    STATUS_CHOISES = (
        ("Undefined", "Undefined"),
        ("Coach", "Coach"),
        ("Manager", "Manager"),
        ("Receptionist", "Receptionist"),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=12, default="YourPhone")
    picture = models.ImageField(upload_to="users/", default="default_user.jpg", blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOISES, default="Undefined")

    def __str__(self):
        return f"{self.user}, status: {self.status}"

    def save(self, *args, **kwargs):
        super(Manager, self).save(*args, **kwargs)

        img = Image.open(self.picture.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.picture.path)


class Group(models.Model):
    group_name = models.CharField(max_length=100)
    age = models.CharField(max_length=20)
    coach = models.ForeignKey(Manager, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.group_name}, {self.age}, {str(self.coach)}"


class Post(models.Model):
    slug = models.SlugField(default="default_slug")
    picture = models.ImageField(upload_to="articles/", default="default.jpg")
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})

    def __str__(self):
        return f"{self.title}, {self.author}, {str(self.date_posted)}"

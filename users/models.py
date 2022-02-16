from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class StudentsGroup(models.Model):
    group_name = models.CharField(max_length=100, default="NewGroup", unique=True)
    coach = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)




class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=12, default="YourPhone")
    picture = models.ImageField(upload_to="users/", default="default_user.jpg", blank=True)
    group = models.ForeignKey(StudentsGroup, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.user}"

    def save(self, *args, **kwargs):
        super(Student, self).save(*args, **kwargs)

        img = Image.open(self.picture.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.picture.path)


class Parent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=12, default="YourPhone")
    picture = models.ImageField(upload_to="users/", default="default_user.jpg", blank=True)

    def __str__(self):
        return f"{self.user}"

    def save(self, *args, **kwargs):
        super(Parent, self).save(*args, **kwargs)

        img = Image.open(self.picture.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.picture.path)

class Relationship(models.Model):
    child = models.ForeignKey(Student, on_delete=models.SET_NULL, null=True)
    parent = models.ForeignKey(Parent, on_delete=models.SET_NULL, null=True)

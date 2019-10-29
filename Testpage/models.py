from django.db import models


class UserProfile(models.Model):
    Name = models.CharField(max_length=200)
    Mail = models.CharField(max_length=200)
    date = models.DateField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return self.Name
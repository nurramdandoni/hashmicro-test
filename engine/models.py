from django.db import models

class Module(models.Model):
    name = models.CharField(max_length=255, unique=True)
    installed = models.BooleanField(default=False)

    def __str__(self):
        return self.name

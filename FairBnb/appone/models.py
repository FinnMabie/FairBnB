from django.db import models
from django.conf import settings


# Model for when users save a property they are interested in
class Property(models.Model):
    zip_code = models.IntegerField(null=False)
    address = models.CharField(null=False, max_length=100)
    user = models.ManyToManyField(settings.AUTH_USER_MODEL, null=True)

    def __str__(self):
        return str(self.address) + ', ' + str(self.zip_code)

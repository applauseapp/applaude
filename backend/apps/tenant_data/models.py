from django.db import models

class TenantData(models.Model):
    key = models.CharField(max_length=100)
    value = models.TextField()

    def __str__(self):
        return self.key

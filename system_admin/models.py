from django.db import models

# Create your models here.

class BusBrand(models.Model):
    name = models.CharField(max_length=50)
    head = models.CharField(max_length = 50)
    number_buses = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created', '-updated')

    def __str__(self):
        return self.name
    



import uuid
from django.db import models
from django.contrib.auth.models import User

class ObjectEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.TextField()
    rating = models.DecimalField(max_digits=3, decimal_places=2)  

    def __str__(self):
        return self.name
from django.db import models
import uuid

class UserDetails(models.Model):
    result = models.CharField(max_length=50)
    result_id = models.UUIDField(
        primary_key = True, 
        default = uuid.uuid4,
        editable = False, 
        unique=True
        )
    status = models.CharField(max_length=50)
    timeout = models.PositiveIntegerField(default=0)

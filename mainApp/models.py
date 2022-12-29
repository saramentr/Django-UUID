from django.db import models
import uuid

class UserDetails(models.Model):
    id = models.UUIDField(
        primary_key = True, 
        default = uuid.uuid4,
        editable = False, 
        unique=True
        )
    name = models.CharField(max_length=50)
    bank_ac_number = models.PositiveIntegerField(default=0)
    paypal_number = models.PositiveIntegerField(default=0)
    ifsc_code = models.CharField(max_length=50)

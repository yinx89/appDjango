from __future__ import unicode_literals
import uuid
from django.db import models


class Photo(models.Model):
    title = models.CharField(max_length=255, blank=True)
    file = models.FileField(upload_to='testapp/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    randomUrl = models.UUIDField(default=uuid.uuid4)
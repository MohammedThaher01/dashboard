from django.db import models

class Event(models.Model):
    type = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)
    metadata = models.JSONField(null=True, blank=True)

    def __str__(self):
        return f"{self.type} @ {self.timestamp}"

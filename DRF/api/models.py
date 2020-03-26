from django.db import models

class Heartbeat(models.Model):
    healthy = models.BooleanField(default=True)

    def __str__(self):
        return self.healthy.__str__()
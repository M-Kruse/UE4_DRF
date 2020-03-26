import uuid 
from django.db import models

class Player(models.Model):
    player_id = models.UUIDField(
            default = uuid.uuid4,
            editable = False
    )
    create_date = models.DateTimeField(auto_now_add=True, editable=False)
    
class Ban(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE, blank=True)
    ban_id = models.UUIDField(
        default = uuid.uuid4,
        editable = False
    )
    ban_date = models.DateTimeField(auto_now_add=True, editable=False)
    reason = models.CharField(max_length=256, default='')
    

class Session(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE, blank=True)
    session_id = models.UUIDField(
        default = uuid.uuid4,
        editable = False
    )
    
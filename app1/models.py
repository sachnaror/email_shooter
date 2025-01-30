from django.db import models
from django.utils.timezone import now

class EmailLog(models.Model):
    recipient = models.EmailField(unique=True)
    sent_at = models.DateTimeField(auto_now_add=True)
    opened = models.BooleanField(default=False)
    clicked_link = models.BooleanField(default=False)
    subject = models.CharField(max_length=100)  # Stores the subject line

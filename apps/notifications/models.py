from datetime import timezone
from django.db import models
from apps.users.models import UUIDModel, User
from apps.admissions.utils import NOTIFICATION_TYPES


class Notification(UUIDModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=255)
    message = models.TextField()
    type = models.CharField(max_length=20, choices=NOTIFICATION_TYPES, default='info')
    is_read = models.BooleanField(default=False)
    send_time = models.DateTimeField(auto_now_add=True)
    read_time = models.DateTimeField(null=True, blank=True)

    def mark_as_read(self):
        self.is_read = True
        self.read_time = timezone.now()
        self.save()

    def __str__(self):
        return f"{self.title} → {self.user.username if self.user else 'Broadcast'}"

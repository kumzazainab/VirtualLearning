from django.db import models
from apps.users.models import UUIDModel
from apps.admissions.utils import SEMESTER_CHOICES, EVENT_TYPE_CHOICES


class AcademicCalendar(UUIDModel):
    title = models.CharField(max_length=255)
    academic_year = models.CharField(max_length=9)
    semester = models.CharField(max_length=20, choices=SEMESTER_CHOICES)
    start_date = models.DateField()
    end_date = models.DateField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.title} ({self.academic_year} - {self.semester})"


class AcademicEvent(UUIDModel):
    calendar = models.ForeignKey(AcademicCalendar, on_delete=models.CASCADE, related_name='events')
    event_type = models.CharField(max_length=50, choices=EVENT_TYPE_CHOICES)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f"{self.title} ({self.event_type})"

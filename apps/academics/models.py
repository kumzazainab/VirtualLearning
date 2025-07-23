from django.db import models
from apps.users.models import UUIDModel, StudentProfile, TeacherProfile
from apps.admissions.utils import DAY_OF_WEEK_CHOICES, ENROLLMENT_STATUS


class AcademicYear(UUIDModel):
    year = models.CharField(max_length=9, unique=True)  # Example: 2025-2026
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.year


class Semester(UUIDModel):
    name = models.CharField(max_length=50)  # Example: Spring, Fall
    academic_year = models.ForeignKey('AcademicYear', on_delete=models.CASCADE, related_name='semesters')
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f"{self.name} {self.academic_year.year}"


class Program(UUIDModel):
    name = models.CharField(max_length=255, unique=True)
    code = models.CharField(max_length=20, unique=True)  # e.g. BSCS-2025
    description = models.TextField(blank=True, null=True)
    duration_years = models.PositiveIntegerField(default=4)

    def __str__(self):
        return self.name


class Course(UUIDModel):
    code = models.CharField(max_length=20, unique=True)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    credit_hours = models.PositiveIntegerField()
    department = models.CharField(max_length=255)
    program = models.ForeignKey('Program', on_delete=models.CASCADE, related_name='courses', null=True, blank=True)
    semester = models.ForeignKey('Semester', on_delete=models.SET_NULL, related_name='courses', null=True, blank=True)
    teacher = models.ForeignKey('users.TeacherProfile', on_delete=models.SET_NULL, null=True, blank=True, related_name='courses')

    def __str__(self):
        return f"{self.code} - {self.title}"


class Lecture(UUIDModel):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="lectures")
    teacher = models.ForeignKey('users.TeacherProfile', on_delete=models.SET_NULL, null=True, blank=True, related_name="lectures")
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True, null=True)
    video_url = models.URLField(blank=True, null=True)
    lecture_date = models.DateField()

    def __str__(self):
        return f"{self.title} ({self.course.code})"


class Schedule(UUIDModel):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="schedules")
    day_of_week = models.CharField(max_length=10, choices=DAY_OF_WEEK_CHOICES)
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return f"{self.course.code} - {self.day_of_week} {self.start_time}-{self.end_time}"


class Enrollment(UUIDModel):
    student = models.ForeignKey(StudentProfile, on_delete=models.CASCADE, related_name="enrollments")
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="enrollments")
    semester = models.ForeignKey(Semester, on_delete=models.SET_NULL, null=True, blank=True, related_name='enrollments')
    enrollment_date = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=ENROLLMENT_STATUS, default='enrolled')

    def __str__(self):
        return f"{self.student.user.username} - {self.course.code} ({self.status})"


class CourseMaterial(UUIDModel):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='materials')
    title = models.CharField(max_length=255)
    file = models.FileField(upload_to='course_materials/', blank=True, null=True)
    link = models.URLField(blank=True, null=True)
    material_type = models.CharField(max_length=50, blank=True, null=True)  # Example:PDF, PPT
    description = models.TextField(blank=True, null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} ({self.course.code})"


class LiveSession(UUIDModel):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='live_sessions')
    teacher = models.ForeignKey(TeacherProfile, on_delete=models.CASCADE, related_name='live_sessions')
    title = models.CharField(max_length=255)
    scheduled_at = models.DateTimeField()
    duration_minutes = models.PositiveIntegerField(default=60)
    meeting_link = models.URLField()
    meeting_credentials = models.CharField(max_length=255, blank=True, null=True)
    recording_link = models.URLField(blank=True, null=True)

    def __str__(self):
        return f"{self.title} - {self.course.code}"


class Attendance(UUIDModel):
    student = models.ForeignKey(StudentProfile, on_delete=models.CASCADE, related_name='attendances')
    lecture = models.ForeignKey('Lecture', on_delete=models.CASCADE, related_name='attendances', null=True, blank=True)
    live_session = models.ForeignKey('LiveSession', on_delete=models.CASCADE, related_name='attendances', null=True, blank=True)
    attended = models.BooleanField(default=False)
    attendance_percentage = models.FloatField(default=0.0)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.student.user.username} - {self.lecture.title if self.lecture else self.live_session.title}"
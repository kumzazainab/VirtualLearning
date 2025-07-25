from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from apps.users.models import UUIDModel
from apps.admissions.utils import ADMISSION_STATUS, PAYMENT_STATUS, PAYMENT_METHOD
from apps.academics.models import Program
from apps.users.models import StudentProfile
from django.db.models import JSONField


class AdmissionCriteria(UUIDModel):
    admission = models.ForeignKey('admissions.Admission', on_delete=models.CASCADE, related_name='criteria')
    min_grade = models.CharField(max_length=10, blank=True, null=True)
    required_documents = models.JSONField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Criteria for {self.admission.title}"


class Admission(UUIDModel):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    program = models.ForeignKey(Program, on_delete=models.CASCADE, related_name='admissions', null=True, blank=True)
    semester = models.CharField(max_length=50)
    year = models.PositiveIntegerField()
    start_date = models.DateField()
    end_date = models.DateField()
    total_seats = models.PositiveIntegerField()
    available_seats = models.PositiveIntegerField()
    fee_amount = models.DecimalField(max_digits=10, decimal_places=2)
    is_active = models.BooleanField(default=True)

    def reserve_seat(self):
        if self.available_seats > 0:
            self.available_seats -= 1
            self.save()
        else:
            raise ValueError("No seats available")

    def __str__(self):
        return f"{self.title} ({self.semester} {self.year})"


class AdmissionApplication(UUIDModel):
    admission = models.ForeignKey(Admission, on_delete=models.CASCADE, related_name='applications')
    student = models.ForeignKey(StudentProfile, on_delete=models.CASCADE, related_name='admission_applications')
    program = models.ForeignKey(Program, on_delete=models.CASCADE, related_name='admission_applications')
    status = models.CharField(max_length=20, choices=ADMISSION_STATUS, default='pending')
    applied_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.student.user.username} - {self.program.name} - {self.admission.title}"


class AdmissionPayment(UUIDModel):
    admission_application = models.ForeignKey(AdmissionApplication, on_delete=models.CASCADE, related_name='payments')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateField()
    payment_method = models.CharField(max_length=50, choices=PAYMENT_METHOD)
    payment_status = models.CharField(max_length=20, choices=PAYMENT_STATUS)

    def __str__(self):
        return f"Payment - {self.admission_application}"


class AdmissionPaymentReceipt(UUIDModel):
    admission_payment = models.OneToOneField(AdmissionPayment, on_delete=models.CASCADE, related_name='receipt')
    receipt_number = models.CharField(max_length=255, unique=True)
    receipt_date = models.DateField()
    receipt_amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Receipt - {self.receipt_number}"


class AdmissionLetter(UUIDModel):
    admission_application = models.OneToOneField(AdmissionApplication, on_delete=models.CASCADE, related_name='letter')
    letter_number = models.CharField(max_length=255, unique=True)
    letter_date = models.DateField()
    letter_content = models.TextField()

    def __str__(self):
        return f"Letter - {self.letter_number}"

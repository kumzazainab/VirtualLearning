from django.db import models
from apps.users.models import UUIDModel
from apps.users.models import TeacherProfile, StudentProfile
from apps.admissions.models import AdmissionApplication
from apps.admissions.utils import PAYMENT_METHOD, PAYMENT_STATUS


class StudentFee(UUIDModel):
    admission_application = models.ForeignKey(AdmissionApplication, on_delete=models.CASCADE)
    total_fee = models.DecimalField(max_digits=10, decimal_places=2)
    due_amount = models.DecimalField(max_digits=10, decimal_places=2)
    due_date = models.DateField()
    is_paid = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.admission_application.student.user.username} - {self.total_fee}"


class FeeReceipt(UUIDModel):
    student_fee = models.ForeignKey(StudentFee, on_delete=models.CASCADE, related_name='receipts')
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateField()
    payment_method = models.CharField(max_length=50, choices=PAYMENT_METHOD)
    transaction_reference = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"Receipt - {self.student_fee.admission_application.student.user.username} - {self.amount_paid}"


class FeeChallan(UUIDModel):
    student = models.ForeignKey(StudentProfile, on_delete=models.CASCADE, related_name='fee_challans')
    admission = models.ForeignKey('admissions.AdmissionApplication', on_delete=models.CASCADE)
    semester = models.ForeignKey('academics.Semester', on_delete=models.CASCADE)
    department = models.CharField(max_length=255)
    program = models.CharField(max_length=255)
    challan_number = models.CharField(max_length=100, unique=True)
    issue_date = models.DateField(auto_now_add=True)
    due_date = models.DateField()
    total_fee = models.DecimalField(max_digits=10, decimal_places=2)
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    remaining_fee = models.DecimalField(max_digits=10, decimal_places=2, editable=False)
    status = models.CharField(max_length=20, choices=PAYMENT_STATUS, default='pending')

    def save(self, *args, **kwargs):
        self.remaining_fee = self.total_fee - self.amount_paid
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Challan - {self.challan_number} for {self.student.user.get_full_name()}"


class TeacherSalary(UUIDModel):
    teacher = models.ForeignKey(TeacherProfile, on_delete=models.CASCADE)
    monthly_amount = models.DecimalField(max_digits=10, decimal_places=2)
    effective_from = models.DateField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.teacher.user.username} - {self.monthly_amount}"


class SalaryPayment(UUIDModel):
    teacher_salary = models.ForeignKey(TeacherSalary, on_delete=models.CASCADE, related_name='payments')
    paid_amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_month = models.DateField()
    payment_date = models.DateField(auto_now_add=True)
    payment_method = models.CharField(max_length=50, choices=PAYMENT_METHOD)
    transaction_reference = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.teacher_salary.teacher.user.username} - {self.payment_month}"

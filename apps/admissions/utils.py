ADMISSION_STATUS = [
    ("pending", "Pending"),
    ("approved", "Approved"),
    ("rejected", "Rejected"),
    ("cancelled", "Cancelled"),
]

PAYMENT_STATUS = [
    ('pending', 'Pending'),
    ('paid', 'Paid'),
    ('refunded', 'Refunded'),
    ('installment', 'Installment'),
]

PAYMENT_METHOD = [
    ('cash', 'Cash'),
    ('bank_transfer', 'Bank Transfer'),
    ('credit_card', 'Credit Card'),
    ('debit_card', 'Debit Card'),
    ('online_payment', 'Online Payment Gateway'),
    ('easypaisa', 'Easypaisa'),
    ('jazzcash', 'JazzCash'),
]

DAY_OF_WEEK_CHOICES = [
    ('Monday', 'Monday'),
    ('Tuesday', 'Tuesday'),
    ('Wednesday', 'Wednesday'),
    ('Thursday', 'Thursday'),
    ('Friday', 'Friday'),
    ('Saturday', 'Saturday'),
    ('Sunday', 'Sunday'),
]

ENROLLMENT_STATUS = [
    ('enrolled', 'Enrolled'),
    ('completed', 'Completed'),
    ('dropped', 'Dropped'),
]

SEMESTER_CHOICES = [
    ('spring', 'Spring'),
    ('fall', 'Fall'),
    ('summer', 'Summer'),
]

EVENT_TYPE_CHOICES = [
    ('holiday', 'Holiday'),
    ('exam', 'Exam'),
    ('break', 'Semester Break'),
    ('orientation', 'Orientation'),
    ('result_day', 'Result Day'),
    ('other', 'Other'),
]

NOTIFICATION_TYPES = [
    ('info', 'Info'),
    ('alert', 'Alert'),
    ('reminder', 'Reminder'),
    ('success', 'Success'),
    ('warning', 'Warning'),
    ('error', 'Error'),
]
from django.db import models
from apps.users.models import UUIDModel
from apps.academics.models import Course, Lecture
from apps.users.models import StudentProfile, TeacherProfile
from apps.academics.models import Semester

class AssessmentType(UUIDModel):
    name = models.CharField(max_length=100, unique=True)  # Example: quiz, assignment, exam
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Assessment(UUIDModel):
    title = models.CharField(max_length=255)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    type = models.ForeignKey(AssessmentType, on_delete=models.PROTECT)
    total_marks = models.PositiveIntegerField()
    passing_marks = models.PositiveIntegerField()
    due_date = models.DateTimeField()
    instructions = models.TextField(blank=True, null=True)
    created_by = models.ForeignKey(TeacherProfile, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.title} - {self.course.title}"


class AssessmentQuestion(UUIDModel):
    assessment = models.ForeignKey(Assessment, on_delete=models.CASCADE, related_name='questions')
    question_text = models.TextField()
    marks = models.PositiveIntegerField()
    correct_answer = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Q: {self.question_text}"


class StudentAssessment(UUIDModel):
    student = models.ForeignKey(StudentProfile, on_delete=models.CASCADE)
    assessment = models.ForeignKey(Assessment, on_delete=models.CASCADE)
    submitted_at = models.DateTimeField(auto_now_add=True)
    marks_obtained = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    is_checked = models.BooleanField(default=False)
    feedback = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.student.user.username} - {self.assessment.title}"


class AssessmentAnswer(UUIDModel):
    student_assessment = models.ForeignKey(StudentAssessment, on_delete=models.CASCADE, related_name='answers')
    question = models.ForeignKey(AssessmentQuestion, on_delete=models.CASCADE)
    answer_text = models.TextField()
    marks_awarded = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return f"{self.student_assessment.student.user.username} - Answer to {self.question.id}"


class Result(UUIDModel):
    student = models.ForeignKey('users.StudentProfile', on_delete=models.CASCADE, related_name='results')
    course = models.ForeignKey('academics.Course', on_delete=models.CASCADE, related_name='results')
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE, related_name='results')
    total_marks = models.DecimalField(max_digits=6, decimal_places=2)
    grade = models.CharField(max_length=5)

    def __str__(self):
        return f"{self.student.user.username} - {self.course.code} - {self.grade}"


class AssignmentSubmission(UUIDModel):
    student_assessment = models.ForeignKey('StudentAssessment', on_delete=models.CASCADE, related_name='submissions')
    assessment = models.ForeignKey('Assessment', on_delete=models.CASCADE, related_name='submissions')
    file = models.FileField(upload_to='assignment_submissions/', blank=True, null=True)
    submitted_at = models.DateTimeField(auto_now_add=True)
    feedback = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Submission: {self.student_assessment.student.user.username} - {self.assessment.title}"
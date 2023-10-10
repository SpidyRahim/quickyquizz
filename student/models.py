from django.db import models
from signup.models import Student
from Quiz.models import Quiz

class StudentReview(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    review_text = models.TextField()
    rating = models.PositiveIntegerField(help_text="Rate Between 1 to 7")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review by {self.student.user.username} for {self.quiz.quiz_name}"



from django.db import models
from signup.models import Student
from Quiz.models import Quiz

class Result(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='student_results')
    exam = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='student_results')
    correct = models.PositiveIntegerField()
    submitted_date = models.DateTimeField(auto_now=True)
    qCount = models.PositiveIntegerField(default=0)
    score = models.PositiveIntegerField(default=0)  # Add this field for scores

    def save(self, *args, **kwargs):
        # Calculate the score as a percentage
        if self.qCount > 0:
            self.score = (self.correct / self.qCount) * 100
        super().save(*args, **kwargs)




#notun
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(Student, on_delete=models.CASCADE)
    email = models.EmailField(default='')

    def __str__(self):
        return self.user.username

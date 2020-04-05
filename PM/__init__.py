from djongo import models

class Student(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)

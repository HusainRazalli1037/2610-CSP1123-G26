from django.db import models

class Subject(models.Model):
    name = models.CharField(max_length=100)
    grade = models.CharField(max_length=5)
    merit_point = models.IntegerField()

    def __str__(self):
        return f"{self.name} - {self.grade}"


class Institution(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)

    # NEW FIELDS
    logo = models.ImageField(upload_to='logos/')
    description = models.TextField(blank=True)
    semester_info = models.CharField(max_length=200, blank=True)
    entry_criteria = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Course(models.Model):
    PROGRAM_CHOICES = [
        ('Foundation', 'Foundation'),
        ('Diploma', 'Diploma'),
        ('Degree', 'Degree'),
    ]

    FIELD_CHOICES = [
        ('Engineering', 'Engineering'),
        ('Business', 'Business'),
        ('IT', 'IT'),
    ]

    name = models.CharField(max_length=200)
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE)
    program_type = models.CharField(max_length=50, choices=PROGRAM_CHOICES)
    field = models.CharField(max_length=50, choices=FIELD_CHOICES)

    def __str__(self):
        return self.name


class Scholarship(models.Model):
    name = models.CharField(max_length=200)
    provider = models.CharField(max_length=200)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    description = models.TextField()

    def __str__(self):
        return self.name
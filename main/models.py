from django.db import models

class University(models.Model):
    name = models.CharField(max_length=100, unique=True)
    logo = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.name


class Course(models.Model):
    university = models.ForeignKey(University, on_delete=models.CASCADE)
    code = models.CharField(max_length=50, default='TEMP')
    name = models.CharField(max_length=255)
    level = models.CharField(max_length=50)
    merit = models.FloatField(default=0)
    duration = models.CharField(max_length=50)
    course_type = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Scholarship(models.Model):
    name = models.CharField(max_length=255)
    deadline = models.DateField(blank=True, null=True)

    location = models.CharField(max_length=100, blank=True, null=True)
    level = models.CharField(max_length=100, blank=True, null=True)

    amount = models.CharField(max_length=100, blank=True, null=True)
    scholarship_type = models.CharField(max_length=100, blank=True, null=True)
    contract = models.CharField(max_length=100, blank=True, null=True, default="N/A")

    def __str__(self):
        return self.name
    
class ScholarshipCourse(models.Model):
    scholarship = models.ForeignKey(Scholarship, on_delete=models.CASCADE)
    course_name = models.CharField(max_length=100)

class ScholarshipCriteria(models.Model):
    scholarship = models.ForeignKey(Scholarship, on_delete=models.CASCADE)
    description = models.CharField(max_length=255)


class Visitor(models.Model):
    page = models.CharField(max_length=100)
    ip_address = models.CharField(max_length=100)
    visited_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.page


class MeritResult(models.Model):
    stream = models.CharField(max_length=50)

    bm = models.CharField(max_length=5)
    bi = models.CharField(max_length=5)
    math = models.CharField(max_length=5)
    sejarah = models.CharField(max_length=5)

    package_subject1 = models.CharField(max_length=100)
    package_grade1 = models.CharField(max_length=5)

    package_subject2 = models.CharField(max_length=100)
    package_grade2 = models.CharField(max_length=5)

    best_subject1 = models.CharField(max_length=100)
    best_grade1 = models.CharField(max_length=5)

    best_subject2 = models.CharField(max_length=100)
    best_grade2 = models.CharField(max_length=5)

    koko = models.FloatField()
    merit = models.FloatField()

    def __str__(self):
        return f"{self.stream} - {self.merit}"


class PathwayHub(models.Model):
    FIELD_CHOICES = [
        ('engineering', 'Engineering'),
        ('business', 'Business'),
        ('science', 'Science'),
        ('arts', 'Arts'),
        ('it', 'IT'),
    ]

    field = models.CharField(max_length=50, choices=FIELD_CHOICES)
    location = models.CharField(max_length=100)

    university = models.CharField(max_length=200)
    logo = models.ImageField(upload_to='university_logos/', blank=True, null=True)

    code = models.CharField(max_length=20)
    name = models.CharField(max_length=255)

    level = models.CharField(max_length=50)
    merit = models.FloatField()  # store as number (NOT string %)

    duration = models.CharField(max_length=50)
    course_type = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    

class PathwayAdvisor(models.Model):
    code = models.CharField(max_length=20)
    name = models.CharField(max_length=255)

    level = models.CharField(max_length=50)
    merit = models.FloatField()

    duration = models.CharField(max_length=50)
    course_type = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    

class SubjectCategory(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    

class Subject(models.Model):
    category = models.ForeignKey(SubjectCategory, on_delete=models.CASCADE)

    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    


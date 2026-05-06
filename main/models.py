from django.db import models

# --- UNIVERSITY & GENERAL INFO ---

class University(models.Model):
    name = models.CharField(max_length=100, unique=True)
    logo = models.ImageField(upload_to='university_logos/', blank=True, null=True)

    class Meta:
        verbose_name_plural = "Universities"

    def __str__(self):
        return self.name

class Course(models.Model):
    university = models.ForeignKey(University, on_delete=models.CASCADE, related_name='university_courses')
    code = models.CharField(max_length=50, default='TEMP')
    name = models.CharField(max_length=255)
    level = models.CharField(max_length=50)
    merit = models.FloatField(default=0.0)
    duration = models.CharField(max_length=50)
    course_type = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name} ({self.university.name})"

# --- SCHOLARSHIP SYSTEM ---
# These models are designed to work with your API root

class Scholarship(models.Model):
    title = models.CharField(max_length=255)
    deadline = models.CharField(max_length=100)
    location = models.CharField(max_length=255)
    level = models.CharField(max_length=255)
    amount = models.CharField(max_length=255)
    scholarship_type = models.CharField(max_length=255)
    contract = models.TextField()
    link = models.URLField()
    logo = models.ImageField(
        upload_to='scholarship_logos/',
        blank=True,
        null=True
    )

    def __str__(self):
        return self.title

class ScholarshipCourse(models.Model):
    scholarship = models.ForeignKey(
        Scholarship,
        on_delete=models.CASCADE,
        related_name='courses' # Matches JS data.courses loop
    )
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class ScholarshipCriteria(models.Model):
    scholarship = models.ForeignKey(
        Scholarship,
        on_delete=models.CASCADE,
        related_name='criteria' # Matches JS data.criteria loop[cite: 2]
    )
    text = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = "Scholarship Criteria"

    def __str__(self):
        return self.text

# --- MERIT & ANALYTICS ---

class Visitor(models.Model):
    page = models.CharField(max_length=100)
    ip_address = models.GenericIPAddressField() # More accurate for IPs
    visited_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.page} - {self.visited_at.strftime('%Y-%m-%d %H:%M')}"

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

# --- INFO HUB & ADVISOR ---

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
    merit = models.FloatField() 
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

# --- SUBJECT CONFIGURATION ---

class SubjectCategory(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = "Subject Categories"

    def __str__(self):
        return self.name

class Subject(models.Model):
    category = models.ForeignKey(SubjectCategory, on_delete=models.CASCADE, related_name='subjects')
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
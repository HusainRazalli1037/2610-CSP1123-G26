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

class Scholarship(models.Model):
    title = models.CharField(max_length=255)
    
    # FIXED: Changed from CharField to DateTimeField for real-time tracking
    deadline = models.DateTimeField(
        null=True, 
        blank=True, 
        help_text="Select the date and time when applications close."
    )
    
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
        related_name='courses'
    )
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class ScholarshipCriteria(models.Model):
    scholarship = models.ForeignKey(
        Scholarship,
        on_delete=models.CASCADE,
        related_name='criteria'
    )
    text = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = "Scholarship Criteria"

    def __str__(self):
        return self.text


# --- ANALYTICS & RESULTS ---

class Visitor(models.Model):
    page = models.CharField(max_length=100)
    ip_address = models.GenericIPAddressField()
    visited_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.page} - {self.visited_at.strftime('%Y-%m-%d %H:%M')}"


class MeritResult(models.Model):
    stream = models.CharField(max_length=50)
    bm = models.CharField(max_length=5)
    bi = models.CharField(max_length=5)
    math = models.CharField(max_length=5)
    sejarah = models.CharField(max_length=5)
    
    # FIXED: Package subjects and grades are now completely nullable
    package_subject1 = models.CharField(max_length=100, null=True, blank=True)
    package_grade1 = models.CharField(max_length=5, null=True, blank=True)
    package_subject2 = models.CharField(max_length=100, null=True, blank=True)
    package_grade2 = models.CharField(max_length=5, null=True, blank=True)
    
    # FIXED: Best subjects and grades remain fully nullable
    best_subject1 = models.CharField(max_length=100, null=True, blank=True)
    best_grade1 = models.CharField(max_length=5, null=True, blank=True)
    best_subject2 = models.CharField(max_length=100, null=True, blank=True)
    best_grade2 = models.CharField(max_length=5, null=True, blank=True)
    
    koko = models.FloatField()
    merit = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.stream} - {self.merit}"


# --- INFO HUB & ADVISOR ---

class PathwayHub(models.Model):
    university = models.CharField(max_length=200, blank=True, null=True)
    logo = models.ImageField(upload_to='university_logos/', blank=True, null=True)
    field = models.CharField(max_length=100, blank=True, null=True)
    location = models.CharField(max_length=100)
    code = models.CharField(max_length=20)
    name = models.CharField(max_length=255)
    level = models.CharField(max_length=50)
    merit = models.FloatField() 
    duration = models.CharField(max_length=50)
    course_type = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Pathway Hub Entry"
        verbose_name_plural = "Pathway Hub Entries"

    def __str__(self):
        return f"{self.university} - {self.name}"


class PathwayAdvisor(models.Model):
    field = models.CharField(max_length=50, default="general") 
    location = models.CharField(max_length=100, default="Malaysia") 
    university = models.CharField(max_length=200, blank=True, null=True, default="")
    code = models.CharField(max_length=20, default="")
    name = models.CharField(max_length=255, default="")
    level = models.CharField(max_length=50, default="")
    merit = models.FloatField(default=0.0)
    duration = models.CharField(max_length=50, default="")
    course_type = models.CharField(max_length=50, default="")

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
    

class ContactInquiry(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Inquiry from {self.name} - {self.email}"
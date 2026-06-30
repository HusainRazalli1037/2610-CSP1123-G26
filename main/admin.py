from django.contrib import admin
from django.db.models import Count
from datetime import date
from django.utils.html import format_html

from .models import (
    Visitor,
    Course,
    Scholarship,
    MeritResult,
    University,
    PathwayHub,
    PathwayAdvisor,
    SubjectCategory,
    Subject,
    ScholarshipCourse,
    ScholarshipCriteria
)

# =========================
# INLINES
# =========================

class CourseInline(admin.TabularInline):
    """Allows editing courses directly inside the University page."""
    model = Course
    extra = 1
    fk_name = "university"

class ScholarshipCourseInline(admin.TabularInline):
    """Allows adding courses to a scholarship directly on its edit page."""
    model = ScholarshipCourse
    extra = 3

class ScholarshipCriteriaInline(admin.TabularInline):
    """Allows adding eligibility criteria to a scholarship directly."""
    model = ScholarshipCriteria
    extra = 3


# =========================
# UNIVERSITY ADMIN
# =========================

@admin.register(University)
class UniversityAdmin(admin.ModelAdmin):
    list_display = ('name', 'course_count')
    search_fields = ('name',)
    inlines = [CourseInline]

    def course_count(self, obj):
        # Uses the related_name defined in the Course model
        return obj.university_courses.count()
    course_count.short_description = "Total Courses"


# =========================
# COURSE ADMIN
# =========================

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'university', 'course_type', 'level', 'merit')
    search_fields = ('name', 'code', 'university__name')
    list_filter = ('course_type', 'level', 'university')
    list_per_page = 20


# =========================
# SCHOLARSHIP ADMIN
# =========================

@admin.register(Scholarship)
class ScholarshipAdmin(admin.ModelAdmin):
    """
    Manages Scholarship data. 
    Crucial: Adding courses/criteria here ensures the API sends text strings
    instead of [object Object] to the frontend.
    """
    list_display = (
        'logo_preview',
        'title',
        'deadline',  # FIXED: Displays the date column cleanly in the admin table dashboard
        'location',
        'scholarship_type'
    )
    search_fields = ('title', 'location')
    list_filter = ('scholarship_type', 'level')
    inlines = [ScholarshipCourseInline, ScholarshipCriteriaInline]

    def logo_preview(self, obj):
        if obj.logo:
            return format_html(
                '<img src="{}" width="40" height="40" style="border-radius:4px; object-fit:contain;" />',
                obj.logo.url
            )
        return "No Logo"
    logo_preview.short_description = "Logo"


# =========================
# VISITOR & ANALYTICS ADMIN
# =========================

@admin.register(Visitor)
class VisitorAdmin(admin.ModelAdmin):
    list_display = ('page', 'ip_address', 'visited_at')
    search_fields = ('ip_address', 'page')
    list_filter = ('page', 'visited_at')
    readonly_fields = ('page', 'ip_address', 'visited_at')
    ordering = ('-visited_at',)
    list_per_page = 50


@admin.register(MeritResult)
class MeritResultAdmin(admin.ModelAdmin):
    list_display = ('stream', 'merit', 'koko', 'created_at')
    list_filter = ('stream', 'created_at')
    search_fields = ('stream',)
    readonly_fields = ('created_at',)


# =========================
# PATHWAY & HUB ADMIN
# =========================

@admin.register(PathwayHub)
class PathwayHubAdmin(admin.ModelAdmin):
    """
    Manages the Info Pathway Hub.
    Ensure 'university' field matches the HTML 'alt' text for data to show up.
    """
    list_display = ('logo_preview', 'university', 'code', 'name', 'level', 'merit', 'course_type')
    search_fields = ('name', 'code', 'university')
    list_filter = ('university', 'level', 'course_type')

    def logo_preview(self, obj):
        if obj.logo:
            return format_html(
                '<img src="{}" width="40" height="40" style="border-radius:4px; object-fit:contain;" />',
                obj.logo.url
            )
        return "No Logo"
    logo_preview.short_description = "Logo"


@admin.register(PathwayAdvisor)
class PathwayAdvisorAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'level', 'merit', 'duration', 'course_type')
    search_fields = ('name', 'code')
    list_filter = ('level', 'course_type')


# =========================
# SUBJECT CONFIGURATION
# =========================

@admin.register(SubjectCategory)
class SubjectCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'category')
    search_fields = ('name', 'category__name')
    list_filter = ('category',)


# =========================
# CUSTOM ADMIN DASHBOARD CONTEXT
# =========================

original_each_context = admin.site.each_context

def custom_each_context(request):
    """Injects stats into the sidebar/header of the Admin panel."""
    context = original_each_context(request)

    # Basic Analytics
    total_visits = Visitor.objects.count()
    today_visits = Visitor.objects.filter(visited_at__date=date.today()).count()

    # Find the most visited page
    popular = Visitor.objects.values('page').annotate(
        total=Count('page')
    ).order_by('-total').first()

    context.update({
        'total_visits': total_visits,
        'today_visits': today_visits,
        'universities_count': University.objects.count(),
        'courses_count': Course.objects.count(),
        'scholarships_count': Scholarship.objects.count(),
        'popular_page': popular['page'] if popular else "No Data"
    })

    return context

# Override the default admin context to show custom stats
admin.site.each_context = custom_each_context
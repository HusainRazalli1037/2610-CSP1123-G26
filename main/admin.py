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
# COURSE INLINE (inside University)
# =========================
class CourseInline(admin.TabularInline):
    model = Course
    extra = 1


# =========================
# UNIVERSITY ADMIN
# =========================
@admin.register(University)
class UniversityAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    inlines = [CourseInline]


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
# SCHOLARSHIP ADMIN (FIXED)
# =========================
@admin.register(Scholarship)
class ScholarshipAdmin(admin.ModelAdmin):
    list_display = (
        'logo_preview',
        'title',
        'deadline',
        'location',
        'level'
    )

    def logo_preview(self, obj):
        if obj.logo:
            return format_html(
                '<img src="{}" width="50" height="50" style="border-radius:8px;" />',
                obj.logo.url
            )
        return "No Logo"

    logo_preview.short_description = "Logo"


admin.site.register(ScholarshipCourse)
admin.site.register(ScholarshipCriteria)


# =========================
# VISITOR ADMIN
# =========================
@admin.register(Visitor)
class VisitorAdmin(admin.ModelAdmin):
    list_display = ('page', 'ip_address', 'visited_at')
    search_fields = ('ip_address', 'page')
    list_filter = ('page', 'visited_at')
    readonly_fields = ('page', 'ip_address', 'visited_at')
    ordering = ('-visited_at',)
    list_per_page = 30


# =========================
# MERIT RESULT ADMIN
# =========================
@admin.register(MeritResult)
class MeritResultAdmin(admin.ModelAdmin):
    list_display = ('stream', 'merit', 'koko')
    list_filter = ('stream',)
    search_fields = ('stream',)


# =========================
# PATHWAY HUB ADMIN
# =========================
@admin.register(PathwayHub)
class PathwayHubAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'field', 'university', 'level', 'merit', 'course_type')
    search_fields = ('name', 'code', 'university')
    list_filter = ('field', 'level', 'course_type')


# =========================
# PATHWAY ADVISOR ADMIN
# =========================
@admin.register(PathwayAdvisor)
class PathwayAdvisorAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'level', 'merit', 'duration', 'course_type')
    search_fields = ('name', 'code')
    list_filter = ('level', 'course_type')


# =========================
# SUBJECT CATEGORY ADMIN
# =========================
@admin.register(SubjectCategory)
class SubjectCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


# =========================
# SUBJECT ADMIN
# =========================
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
    context = original_each_context(request)

    total_visits = Visitor.objects.count()

    today_visits = Visitor.objects.filter(
        visited_at__date=date.today()
    ).count()

    popular = Visitor.objects.values('page').annotate(
        total=Count('page')
    ).order_by('-total').first()

    context.update({
        'total_visits': total_visits,
        'today_visits': today_visits,
        'universities': University.objects.count(),
        'courses': Course.objects.count(),
        'scholarships': Scholarship.objects.count(),
        'popular_page': popular['page'] if popular else "No Data"
    })

    return context


admin.site.each_context = custom_each_context
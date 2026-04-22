from django.contrib import admin
from django.contrib.admin import AdminSite
from django.db.models import Count
from datetime import date
from .models import Visitor, Institution, Course, Scholarship


# =========================
# COURSE INLINE
# =========================
class CourseInline(admin.TabularInline):
    model = Course
    extra = 1


# =========================
# INSTITUTION ADMIN
# =========================
@admin.register(Institution)
class InstitutionAdmin(admin.ModelAdmin):
    list_display = ('name', 'location')
    search_fields = ('name', 'location')
    list_filter = ('location',)
    inlines = [CourseInline]


# =========================
# COURSE ADMIN
# =========================
@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'institution', 'program_type', 'field')
    search_fields = ('name', 'institution__name')
    list_filter = ('program_type', 'field', 'institution')
    list_per_page = 20


# =========================
# SCHOLARSHIP ADMIN
# =========================
@admin.register(Scholarship)
class ScholarshipAdmin(admin.ModelAdmin):
    list_display = ('name', 'provider', 'course')
    search_fields = ('name', 'provider')
    list_filter = ('provider',)
    list_per_page = 20


# =========================
# VISITOR ADMIN
# =========================
@admin.register(Visitor)
class VisitorAdmin(admin.ModelAdmin):
    list_display = ('page', 'ip_address', 'visited_at')
    search_fields = ('ip_address',)
    list_filter = ('page', 'visited_at')
    readonly_fields = ('page', 'ip_address', 'visited_at')
    ordering = ('-visited_at',)
    list_per_page = 30

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
        'institutions': Institution.objects.count(),
        'courses': Course.objects.count(),
        'scholarships': Scholarship.objects.count(),
        'popular_page': popular['page'] if popular else "No Data"
    })

    return context


admin.site.each_context = custom_each_context
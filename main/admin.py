from django.contrib import admin
from .models import Subject, Institution, Course, Scholarship

admin.site.register(Subject)
admin.site.register(Institution)
admin.site.register(Course)
admin.site.register(Scholarship)
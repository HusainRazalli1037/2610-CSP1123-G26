from django.contrib import admin
from .models import Subject, Institution, Course, Scholarship
from .models import Visitor

admin.site.register(Subject)
admin.site.register(Institution)
admin.site.register(Course)
admin.site.register(Scholarship)
admin.site.register(Visitor)
from rest_framework import serializers
from .models import (
    PathwayAdvisor,
    Scholarship, 
    ScholarshipCourse, 
    ScholarshipCriteria, 
    PathwayHub
)

# ==========================================
# --- SCHOLARSHIP RELATED SERIALIZERS ---
# ==========================================

class ScholarshipCourseSerializer(serializers.ModelSerializer):
    """
    Serializes the individual courses linked to a scholarship.
    Targeted by myScript2.js using 'c.name'.
    """
    class Meta:
        model = ScholarshipCourse
        fields = ['name']


class ScholarshipCriteriaSerializer(serializers.ModelSerializer):
    """
    Serializes the eligibility criteria for a scholarship.
    Targeted by myScript2.js using 'c.text'.
    """
    class Meta:
        model = ScholarshipCriteria
        fields = ['text']


class ScholarshipSerializer(serializers.ModelSerializer):
    """
    Main Scholarship Serializer.
    Nests related courses and criteria to prevent [object Object] errors.
    'courses' and 'criteria' names must match the 'related_name' in models.py.
    """
    # Nested relations matching the related_name values defined on ForeignKeys
    courses = ScholarshipCourseSerializer(many=True, read_only=True)
    criteria = ScholarshipCriteriaSerializer(many=True, read_only=True)

    class Meta:
        model = Scholarship
        fields = '__all__'


# ==========================================
# --- PATHWAY HUB SERIALIZER ---
# ==========================================

class PathwayHubSerializer(serializers.ModelSerializer):
    """
    Handles data for the Info Pathway Hub.
    Using '__all__' ensures that merit, code, level, duration, 
    and course_type are available for pathwayScript.js.
    """
    class Meta:
        model = PathwayHub
        fields = '__all__'


# ==========================================
# --- PATHWAY ADVISOR SERIALIZER ---
# ==========================================

class PathwayAdvisorSerializer(serializers.ModelSerializer):
    """
    Handles recommendation matching algorithms data for the Pathway Advisor.
    Exposes all filtering criteria fields to the recommendation API viewset.
    """
    class Meta:
        model = PathwayAdvisor
        fields = '__all__'
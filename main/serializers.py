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
    Serializes individual courses linked to a scholarship.
    Ensures 'myScript2.js' can map objects using 'c.name'.
    """
    class Meta:
        model = ScholarshipCourse
        fields = ['name']


class ScholarshipCriteriaSerializer(serializers.ModelSerializer):
    """
    Serializes eligibility criteria for a scholarship.
    Ensures 'myScript2.js' can map objects using 'c.text'.
    """
    class Meta:
        model = ScholarshipCriteria
        fields = ['text']


class ScholarshipSerializer(serializers.ModelSerializer):
    """
    Main Scholarship Serializer.
    Explicitly overrides nested fields to return detailed text blocks 
    instead of raw relational database IDs.
    """
    # The variable names 'courses' and 'criteria' MUST match the related_name 
    # definitions set in your models.py file
    courses = ScholarshipCourseSerializer(many=True, read_only=True)
    criteria = ScholarshipCriteriaSerializer(many=True, read_only=True)

    class Meta:
        model = Scholarship
        fields = [
            'id', 'title', 'deadline', 'logo', 'location', 
            'level', 'amount', 'scholarship_type', 'contract', 
            'link', 'courses', 'criteria'
        ]


# ==========================================
# --- PATHWAY HUB SERIALIZER ---
# ==========================================

class PathwayHubSerializer(serializers.ModelSerializer):
    """
    Handles data for the Info Pathway Hub interface.
    """
    class Meta:
        model = PathwayHub
        fields = '__all__'


# ==========================================
# --- PATHWAY ADVISOR SERIALIZER ---
# ==========================================

class PathwayAdvisorSerializer(serializers.ModelSerializer):
    """
    Handles data structures for recommendation matching filters.
    """
    class Meta:
        model = PathwayAdvisor
        fields = '__all__'
from rest_framework import serializers
from .models import Scholarship, ScholarshipCourse, ScholarshipCriteria

class ScholarshipCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScholarshipCourse
        fields = ['name']

class ScholarshipCriteriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScholarshipCriteria
        fields = ['text']

class ScholarshipSerializer(serializers.ModelSerializer):
    # This nests the related data into the JSON array[cite: 2]
    courses = ScholarshipCourseSerializer(many=True, read_only=True)
    criteria = ScholarshipCriteriaSerializer(many=True, read_only=True)

    class Meta:
        model = Scholarship
        fields = '__all__'
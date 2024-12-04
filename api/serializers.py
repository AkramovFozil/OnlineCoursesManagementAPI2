from rest_framework import serializers
from .models import Course, Instructor, Lesson


class InstructorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Instructor
        fields = ('id', 'name', 'email', 'speciality')

    def validate_email(self, email):
        if Instructor.objects.filter(email=email).exists():
            raise serializers.ValidationError(
                'Email already exists'
            )
        return email


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ('id', 'title', 'description', 'instructor', 'start_date', 'end_date')

    def validate(self, data):
        if not data['start_date'] and not data['end_date']:
            raise serializers.ValidationError(
                'Start date and end date are required'
            )
        return data

    def validate2(self, data):
        if data['start_date'] > data['end_date']:
            raise serializers.ValidationError(
                'Start date must be before end date'
            )
        return data


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ('id', 'title', 'content', 'course', 'order')

    def validate_order(self, order):
        if order <= 0:
            raise serializers.ValidationError(
                'Order must be greater than 0'
            )
        return order

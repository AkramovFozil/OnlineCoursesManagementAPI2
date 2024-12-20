from django.shortcuts import render
from .serializers import CourseSerializer, InstructorSerializer, LessonSerializer
from .models import Course, Instructor, Lesson
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView


# for Curse
class CourseListCreateAPIView(ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class CourseRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


# for Instructor

class InstructorListAPIView(ListCreateAPIView):
    queryset = Instructor.objects.all()
    serializer_class = InstructorSerializer


class InstructorRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Instructor.objects.all()
    serializer_class = InstructorSerializer


# for Lesson
class LessonListCreateAPIView(ListCreateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer


class LessonRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer

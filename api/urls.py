from django.urls import path
from api.views import (
    ScheduleApi,
    SchoolClassApi,
    StudentApi,
    SubjectApi,
    TeacherApi,
)


urlpatterns = [
    path('student', StudentApi.as_view()),
    path('teacher', TeacherApi.as_view()),
    path('subject', SubjectApi.as_view()),
    path('schedule', ScheduleApi.as_view()),
    path('school-class', SchoolClassApi.as_view()),   
]

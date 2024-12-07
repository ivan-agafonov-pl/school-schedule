from django.db.models import Count
from rest_framework.serializers import (
    CharField,
    ModelSerializer,
    SerializerMethodField
)

from api.models import (
    Schedule,
    SchoolClass,
    Student,
    Subject,
    Teacher,
)


# Post Serializers

class TeacherSerializerPost(ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'


class SchoolClassSerializerPost(ModelSerializer):
    class Meta:
        model = SchoolClass
        fields = '__all__'


class StudentSerializerPost(ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'


class SubjectSerializerPost(ModelSerializer):
    class Meta:
        model = Subject
        fields = '__all__'


class ScheduleSerializerPost(ModelSerializer):
    class Meta:
        model = Schedule
        fields = '__all__'


# Get Serializers

class SchoolClassSerializerGet(ModelSerializer):
    student_count = SerializerMethodField()
    def get_student_count(self, obj):
        return obj.students.count()

    class Meta:
        model = SchoolClass
        fields = ['name', 'student_count']


class ScheduleSerializerGet(ModelSerializer):
    school_class = SchoolClassSerializerGet()

    subject = SerializerMethodField()
    def get_subject(self, obj):
        return {'name': obj.subject.name}

    teacher = SerializerMethodField()
    def get_teacher(self, obj):
        return {'name': obj.subject.teacher.name}

    class Meta:
        model = Schedule
        fields = ['school_class', 'subject', 'day_of_week', 'hour', 'teacher']

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['class'] = data.pop('school_class')
        return data

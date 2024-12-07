from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models import (
	CharField,
	ForeignKey,
	IntegerField,
	ManyToManyField,
	Model,
	CASCADE
)


class SchoolClass(Model):
	name = CharField(max_length=10)


class Student(Model):
	name = CharField(max_length=10)
	school_class = ForeignKey(SchoolClass, related_name='students', on_delete=CASCADE)


class Teacher(Model):
	name = CharField(max_length=10)


class Subject(Model):
	name = CharField(max_length=10)
	teacher = ForeignKey(Teacher, on_delete=CASCADE)


class Schedule(Model):
	class Meta:
		ordering = ['day_of_week', 'hour']

	subject = ForeignKey(Subject, on_delete=CASCADE)
	school_class = ForeignKey(SchoolClass, on_delete=CASCADE)
	day_of_week = IntegerField(
		validators=[MinValueValidator(1), MaxValueValidator(7)]  # Monday - Sunday
	)
	hour = IntegerField(
		validators=[MinValueValidator(9), MaxValueValidator(18)]  # 09:00 - 18:00
	)

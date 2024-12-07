from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.status import (
	HTTP_200_OK,
	HTTP_201_CREATED,
	HTTP_400_BAD_REQUEST
)

from api.queries import get_schedule
from api.serializers import (
	ScheduleSerializerGet,
	ScheduleSerializerPost,
	SchoolClassSerializerPost,
	StudentSerializerPost,
	SubjectSerializerPost,
	TeacherSerializerPost,
)


class ApiBase(APIView):
	def post(self, request):
		serializer = self.post_serializer(data=request.data)

		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=HTTP_201_CREATED)
		return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


class ScheduleApi(ApiBase):
	post_serializer = ScheduleSerializerPost

	def get(self, request):
		schedule = get_schedule(
			for_today=request.GET.get('for_today'),
			class_name=request.GET.get('class_name')
		)
		serializer = ScheduleSerializerGet(schedule, many=True)
		return Response(serializer.data, status=HTTP_200_OK)


class StudentApi(ApiBase):
	post_serializer = StudentSerializerPost


class TeacherApi(ApiBase):
	post_serializer = TeacherSerializerPost


class SubjectApi(ApiBase):
	post_serializer = SubjectSerializerPost


class SchoolClassApi(ApiBase):
	post_serializer = SchoolClassSerializerPost


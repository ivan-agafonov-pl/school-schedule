import datetime, random

from django.test import Client, TestCase
from rest_framework import status


class TestSchoolScheduleApi(TestCase):
    api_client = Client()
    api_schedule_url = '/api/schedule'

    @classmethod
    def setUpClass(cls):
        super().setUpClass()

        class_1_id = cls.api_client.post('/api/school-class', {'name': 'Class 1'}).data['id']
        class_2_id = cls.api_client.post('/api/school-class', {'name': 'Class 2'}).data['id']
        class_3_id = cls.api_client.post('/api/school-class', {'name': 'Class 3'}).data['id']

        teacher_1_id = cls.api_client.post('/api/teacher', {'name': 'Teacher 1'}).data['id']
        teacher_2_id = cls.api_client.post('/api/teacher', {'name': 'Teacher 2'}).data['id']
        teacher_3_id = cls.api_client.post('/api/teacher', {'name': 'Teacher 3'}).data['id']

        subject_1_id = cls.api_client.post('/api/subject', {'name': 'Subject 1', 'teacher': teacher_1_id}).data['id']
        subject_2_id = cls.api_client.post('/api/subject', {'name': 'Subject 2', 'teacher': teacher_2_id}).data['id']
        subject_3_id = cls.api_client.post('/api/subject', {'name': 'Subject 3', 'teacher': teacher_2_id}).data['id']
        subject_4_id = cls.api_client.post('/api/subject', {'name': 'Subject 4', 'teacher': teacher_3_id}).data['id']

        cls.api_client.post('/api/student', {'name': 'Student 1', 'school_class': class_1_id})
        cls.api_client.post('/api/student', {'name': 'Student 2', 'school_class': class_2_id})
        cls.api_client.post('/api/student', {'name': 'Student 3', 'school_class': class_2_id})
        cls.api_client.post('/api/student', {'name': 'Student 4', 'school_class': class_3_id})
        cls.api_client.post('/api/student', {'name': 'Student 5', 'school_class': class_2_id})

        cls.api_client.post(cls.api_schedule_url, {'subject': subject_1_id, 'school_class': class_1_id, 'day_of_week': 1, 'hour': 13})
        cls.api_client.post(cls.api_schedule_url, {'subject': subject_1_id, 'school_class': class_2_id, 'day_of_week': 2, 'hour': 13})
        cls.api_client.post(cls.api_schedule_url, {'subject': subject_2_id, 'school_class': class_3_id, 'day_of_week': 3, 'hour': 10})
        cls.api_client.post(cls.api_schedule_url, {'subject': subject_2_id, 'school_class': class_1_id, 'day_of_week': 4, 'hour': 9})
        cls.api_client.post(cls.api_schedule_url, {'subject': subject_3_id, 'school_class': class_2_id, 'day_of_week': 5, 'hour': 17})
        cls.api_client.post(cls.api_schedule_url, {'subject': subject_3_id, 'school_class': class_3_id, 'day_of_week': 1, 'hour': 16})
        cls.api_client.post(cls.api_schedule_url, {'subject': subject_3_id, 'school_class': class_1_id, 'day_of_week': 2, 'hour': 16})
        cls.api_client.post(cls.api_schedule_url, {'subject': subject_4_id, 'school_class': class_2_id, 'day_of_week': 3, 'hour': 15})
        cls.api_client.post(cls.api_schedule_url, {'subject': subject_4_id, 'school_class': class_2_id, 'day_of_week': 3, 'hour': 12})
        cls.api_client.post(cls.api_schedule_url, {'subject': subject_3_id, 'school_class': class_3_id, 'day_of_week': 1, 'hour': 9})

    def test_schedule_response_schema_validation(self):
        response = self.api_client.get(self.api_schedule_url)
        schedule = random.choice(response.data)

        assert isinstance(schedule['class']['name'], str)
        assert isinstance(schedule['class']['student_count'], int)
        assert isinstance(schedule['subject']['name'], str)
        assert isinstance(schedule['day_of_week'], int)
        assert isinstance(schedule['hour'], int)
        assert isinstance(schedule['teacher']['name'], str)

    def test_schedule_total_class_count(self):
        response = self.api_client.get(self.api_schedule_url)
        assert len(response.data) == 10

    def test_schedule_is_ordered_by_day_of_week_and_then_by_hour(self):
        response = self.api_client.get(self.api_schedule_url)
        assert response.data[0]['day_of_week'] == 1
        assert response.data[9]['day_of_week'] == 5
        assert response.data[0]['hour'] < response.data[1]['hour'] < response.data[2]['hour']

    def test_schedule_returns_result_only_for_today(self):
        response = self.api_client.get(self.api_schedule_url, {'for_today': True})
        today = int(datetime.datetime.today().strftime('%w'))
        for item in response.data:
            assert item['day_of_week'] == today

    def test_schedule_returns_result_only_for_selected_class_name(self):
        class_name = 'Class 1'
        response = self.api_client.get(self.api_schedule_url, {'class_name': class_name})
        for item in response.data:
            assert item['class']['name'] == class_name

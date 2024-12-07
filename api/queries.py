import datetime
from api.models import Schedule


def get_schedule(for_today=None, class_name=None):
	query = Schedule.objects.all()
	if for_today:
		today = int(datetime.datetime.today().strftime('%w'))  # Monday - Sunday (1 - 7)
		query = query.filter(day_of_week=today)
	if class_name:
		query = query.filter(school_class__name=class_name)
	return query

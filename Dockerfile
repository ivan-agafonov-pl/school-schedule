FROM python:3.13

WORKDIR /school_schedule

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["sh", "-c", "python manage.py migrate && python manage.py test --verbosity=0"]

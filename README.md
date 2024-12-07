### How to run the app?

1) Clone repo: 'git clone https://github.com/ivan-agafonov-pl/school-schedule.git'
2) Go inside the school-schedule directory
3) Run 'docker-compose up --build school_schedule_tests'

### What's just happened?

You just run 5 tests which is relevant to this project. You should see
in output of 'docker-compose up school_schedule_tests' they are successful.

### How to debug / check stuff more in deep?

You can go to school_schedule -> api -> tests.py and check content there.
It's pretty self-explanatory so you can tweak some test data and make sure everything is
still working by running 'docker-compose up --build school_schedule_tests'

### Few points to consider while reviewing my home assignment

1) At this point application doesnt resist to any kind of perfomance wise loads.
Meaning it's not production ready. To make sure we can deploy it to the production we need
at least:
- set up and configure Nginx
- set up and configure some Python webserver (Gunicorn or another one)
- set up and configure something like Pgbouncer for managing Postgresql connections
- tweak some Django settings
- run perfomance tests against it (Locust or custome ones)

2) My point is typing and lintering are very crucial practices in any good project,
I didnt introduce them here but it's worth to mention.
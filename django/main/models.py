from datetime import timedelta

from django.db import models
from django.utils import timezone

"""
{
    "assignment": {
        "id": 3053267,
        "name": "testing 123",
        "type": "input_output"
    },
    "classroom": {
        "id": 127262,
        "name": "testing webhooks",
        "webhook_secret": "9b200c62-dff3-480f-90ef-8d8884912067"
    },
    "submission": {
        "id": 6231499,
        "status": "complete",
        "time_submitted": "2019-04-02T19:02:42.490Z",
        "time_created": "2019-04-02T19:02:37.000Z",
        "teacher_url": "https://repl.it/teacher/submissions/6231499",
        "student_url": "https://repl.it/student/submissions/6231499",
        "files": [
            {
                "name": "main.py",
                "content": "print(\"hello\")\n# another submission"
            }
        ]
    },
    "student": {
        "id": 1728357,
        "first_name": "Dan",
        "last_name": "Gallo",
        "email": "dangallo110@gmail.com"
    },
    "event_name": "student_submits_assignment"
}
"""
# Create your models here.
class Submission(models.Model):
    submission_id = models.IntegerField()
    classroom_name = models.TextField()
    assignment_name = models.TextField()
    status = models.TextField()
    time_submitted = models.DateTimeField()
    code = models.TextField()
    student_name = models.TextField()
    student_email = models.EmailField()

    # TODO: Add submission url

    @staticmethod
    def parse_from_webhook_data(data) -> "Submission":
        sub = Submission()
        sub.submission_id = data['submission']['id']
        sub.classroom_name = data['classroom']['name']
        sub.assignment_name = data['assignment']['name']
        sub.status = data['submission']['status']
        sub.time_submitted = data['submission']['time_submitted']
        sub.code = data['submission']['files'][0]['content']
        sub.student_name = data['student']['first_name'] + " " + data['student']['last_name']
        sub.student_email = data['student']['email']
        sub.save()

        return sub
    
    @staticmethod
    def generate_fixtures(users=None, assignments=None):
        users = users or [f"user{n}" for n in range(3)]
        assignments = assignments or [f"Assignment{n}" for n in range(3)]

        user_assignments = [(user, assign, f"{user}@ycdsbk12.ca") for user in users
                                                                  for assign in assignments]

        now = timezone.now()
        minute = timedelta(minutes=1)
        fixtures = []
        for i, (user, assign, email) in enumerate(user_assignments):
            sub = Submission(student_name=user,
                             student_email=email,
                             classroom_name="Fixtures",
                             assignment_name=assign,
                             time_submitted=now-minute*i,
                             status=("completed", "awaiting help", "no progress")[i%3],
                             code=f"code{i}",
                             submission_id=i*1000)
            sub.save()
            fixtures.append(sub)
        return fixtures


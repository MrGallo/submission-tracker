from django.urls import path
from main import views


urlpatterns = [
  path("", views.home, name='home'),
  path("submit/", views.submit, name='submit'),
  path("submissions/<int:submission_id>/", views.submission, name='submission-detail'),
  path("create-fixtures/", views.create_fixtures, name='create-fixtures'),
  path("students/<str:student_name>/", views.student_detail, name='student-detail'),
  path("classrooms/<str:classroom_name>/", views.classroom_detail, name='classroom-detail'),
]

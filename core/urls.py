from django.urls import path
from .views import TaskListView, TaskDetailView

# These are the URL patterns for the 'core' app.
# They will be mounted under /api/ by the main project urls.py
urlpatterns = [
    # /api/tasks/       → TaskListView  (GET all, POST new)
    path('tasks/', TaskListView.as_view(), name='task-list'),

    # /api/tasks/1/     → TaskDetailView (GET one, PUT update, DELETE delete)
    # <int:pk> is a URL parameter — Django captures the number and passes it to the view as 'pk'
    path('tasks/<int:pk>/', TaskDetailView.as_view(), name='task-detail'),
]

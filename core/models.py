from django.db import models


class Task(models.Model):
    """
    Represents a single task in our Task Manager.
    Each field here becomes a column in the database table.
    """
    title = models.CharField(max_length=200)          # Short text, max 200 chars
    description = models.TextField(blank=True)         # Longer text, can be empty
    completed = models.BooleanField(default=False)     # True/False, defaults to False
    created_at = models.DateTimeField(auto_now_add=True)  # Set automatically on creation

    def __str__(self):
        # This controls how a Task object is displayed (e.g. in the admin panel)
        return self.title

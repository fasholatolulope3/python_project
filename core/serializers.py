from rest_framework import serializers
from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    """
    Serializer for the Task model.

    ModelSerializer automatically generates fields that match our model.
    We just need to tell it:
      - Which model to use (model = Task)
      - Which fields to include in the API response (fields = '__all__' means all of them)
    """
    class Meta:
        model = Task
        fields = '__all__'  # Includes: id, title, description, completed, created_at

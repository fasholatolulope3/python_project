from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Task
from .serializers import TaskSerializer


class TaskListView(APIView):
    """
    Handles requests to /api/tasks/

    GET  → Returns a list of ALL tasks as JSON
    POST → Creates a NEW task from the JSON body sent in the request
    """

    def get(self, request):
        # Fetch all Task rows from the database
        tasks = Task.objects.all()
        # Convert the queryset to JSON using our serializer
        # many=True means we're serializing a list, not a single object
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)

    def post(self, request):
        # Take the incoming JSON data and pass it to the serializer to validate
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()  # Saves the new Task to the database
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # If validation fails, return the errors with a 400 Bad Request status
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TaskDetailView(APIView):
    """
    Handles requests to /api/tasks/<id>/

    GET    → Returns a SINGLE task by its ID
    PUT    → Updates an existing task
    DELETE → Deletes a task
    """

    def get_object(self, pk):
        """Helper method to fetch a task by primary key (ID), or 404 if not found."""
        try:
            return Task.objects.get(pk=pk)
        except Task.DoesNotExist:
            return None

    def get(self, request, pk):
        task = self.get_object(pk)
        if task is None:
            return Response({'error': 'Task not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = TaskSerializer(task)
        return Response(serializer.data)

    def put(self, request, pk):
        task = self.get_object(pk)
        if task is None:
            return Response({'error': 'Task not found'}, status=status.HTTP_404_NOT_FOUND)
        # Pass existing task + new data, partial=False means all required fields must be sent
        serializer = TaskSerializer(task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        task = self.get_object(pk)
        if task is None:
            return Response({'error': 'Task not found'}, status=status.HTTP_404_NOT_FOUND)
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

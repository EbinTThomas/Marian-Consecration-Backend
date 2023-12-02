from django.db import models

import uuid
from django.db import models
from django.contrib.auth.models import User

class Consecration(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=100)
    start_date = models.DateField()

class Day(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    day_number = models.PositiveIntegerField()
    prayers = models.TextField()  # Store prayers as text
    reflections = models.TextField()  # Store reflections as text

class UserProgress(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    day = models.ForeignKey(Day, on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)

class books(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=100)
    content = models.TextField()
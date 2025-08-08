from djongo import models

class User(models.Model):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)

class Team(models.Model):
    name = models.CharField(max_length=128, unique=True)
    members = models.ArrayReferenceField(to=User, on_delete=models.CASCADE)

class Activity(models.Model):
    activity_id = models.CharField(max_length=128, unique=True)
    duration = models.DurationField()

class Leaderboard(models.Model):
    leaderboard_id = models.CharField(max_length=128, unique=True)
    score = models.IntegerField()

class Workout(models.Model):
    workout_id = models.CharField(max_length=128, unique=True)
    description = models.TextField()
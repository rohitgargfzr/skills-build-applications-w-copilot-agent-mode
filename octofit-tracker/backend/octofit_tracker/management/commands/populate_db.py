from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the database with test data for users, teams, activity, leaderboard, and workouts'

    def handle(self, *args, **kwargs):
        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Add test users
        user1 = User.objects.create(email="user1@example.com", password="password1")
        user2 = User.objects.create(email="user2@example.com", password="password2")

        # Add test teams
        team1 = Team.objects.create(name="Team Alpha")
        team1.members.add(user1, user2)

        # Add test activities
        Activity.objects.create(activity_id="run1", duration="00:30:00")

        # Add test leaderboard
        Leaderboard.objects.create(leaderboard_id="lb1", score=100)

        # Add test workouts
        Workout.objects.create(workout_id="workout1", description="Morning Yoga")

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data'))

from django.test import TestCase
from .models import Team, Activity, Leaderboard, Workout
from django.contrib.auth.models import User

class ModelTests(TestCase):
    def test_team_creation(self):
        team = Team.objects.create(name='TestTeam')
        self.assertEqual(team.name, 'TestTeam')

    def test_activity_creation(self):
        activity = Activity.objects.create(name='TestActivity', user_email='test@example.com', team='TestTeam')
        self.assertEqual(activity.name, 'TestActivity')

    def test_leaderboard_creation(self):
        leaderboard = Leaderboard.objects.create(team='TestTeam', points=50)
        self.assertEqual(leaderboard.points, 50)

    def test_workout_creation(self):
        workout = Workout.objects.create(name='TestWorkout', difficulty='Easy')
        self.assertEqual(workout.difficulty, 'Easy')

    def test_user_creation(self):
        user = User.objects.create_user(username='testuser', email='testuser@example.com', password='testpass')
        self.assertEqual(user.email, 'testuser@example.com')

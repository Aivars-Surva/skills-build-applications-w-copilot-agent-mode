
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from octofit_tracker.models import Team, Activity, Leaderboard, Workout

User = get_user_model()

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Delete existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Create teams
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # Create users (super heroes)
        users = [
            {'email': 'ironman@marvel.com', 'username': 'IronMan', 'team': 'Marvel'},
            {'email': 'captain@marvel.com', 'username': 'CaptainAmerica', 'team': 'Marvel'},
            {'email': 'batman@dc.com', 'username': 'Batman', 'team': 'DC'},
            {'email': 'wonderwoman@dc.com', 'username': 'WonderWoman', 'team': 'DC'},
        ]
        for u in users:
            if not User.objects.filter(email=u['email']).exists():
                User.objects.create_user(email=u['email'], username=u['username'], password='password')

        # Create activities
        activities = [
            {'name': 'Running', 'user_email': 'ironman@marvel.com', 'team': 'Marvel'},
            {'name': 'Swimming', 'user_email': 'captain@marvel.com', 'team': 'Marvel'},
            {'name': 'Cycling', 'user_email': 'batman@dc.com', 'team': 'DC'},
            {'name': 'Yoga', 'user_email': 'wonderwoman@dc.com', 'team': 'DC'},
        ]
        for a in activities:
            Activity.objects.create(**a)

        # Create leaderboard
        Leaderboard.objects.create(team='Marvel', points=100)
        Leaderboard.objects.create(team='DC', points=90)

        # Create workouts
        workouts = [
            {'name': 'Pushups', 'difficulty': 'Medium'},
            {'name': 'Squats', 'difficulty': 'Easy'},
            {'name': 'Deadlift', 'difficulty': 'Hard'},
        ]
        for w in workouts:
            Workout.objects.create(**w)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data'))

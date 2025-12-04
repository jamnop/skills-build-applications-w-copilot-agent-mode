from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard
from django.utils import timezone

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):

        # Drop collections directly for Djongo/MongoDB compatibility
        from django.db import connection
        db = connection.cursor().db_conn.client['octofit_db']
        db['leaderboard'].drop()
        db['activity'].drop()
        db['user'].drop()
        db['team'].drop()
        db['workout'].drop()

        # Create Teams
        marvel = Team.objects.create(name='Team Marvel', universe='Marvel')
        dc = Team.objects.create(name='Team DC', universe='DC')

        # Create Users (Superheroes)
        users = []
        users.append(User.objects.create(name='Spider-Man', email='spiderman@marvel.com', team=marvel))
        users.append(User.objects.create(name='Iron Man', email='ironman@marvel.com', team=marvel))
        users.append(User.objects.create(name='Wonder Woman', email='wonderwoman@dc.com', team=dc))
        users.append(User.objects.create(name='Batman', email='batman@dc.com', team=dc))

        # Create Workouts
        workouts = []
        workouts.append(Workout.objects.create(name='Super Strength', description='Strength training for superheroes', difficulty='Hard'))
        workouts.append(Workout.objects.create(name='Flight Training', description='Aerial maneuvers and stamina', difficulty='Medium'))

        # Create Activities
        for user in users:
            Activity.objects.create(user=user, activity_type='Running', duration_minutes=30, date=timezone.now().date())
            Activity.objects.create(user=user, activity_type='Weight Lifting', duration_minutes=45, date=timezone.now().date())

        # Create Leaderboard
        for i, user in enumerate(users):
            Leaderboard.objects.create(user=user, score=100-i*10, rank=i+1)

        self.stdout.write(self.style.SUCCESS('octofit_db populated with test data!'))

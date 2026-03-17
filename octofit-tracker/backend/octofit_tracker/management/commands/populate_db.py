from django.core.management.base import BaseCommand

from octofit_tracker.models import Activity, Leaderboard, Team, User, Workout


class Command(BaseCommand):
    help = 'octofit_db 데이터베이스에 테스트 데이터를 입력합니다.'

    def handle(self, *args, **options):
        self.stdout.write(self.style.WARNING('기존 테스트 데이터 정리 중...'))
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()
        Team.objects.all().delete()
        User.objects.all().delete()

        marvel = Team.objects.create(name='Marvel Team', city='New York', mascot='Avengers')
        dc = Team.objects.create(name='DC Team', city='Gotham', mascot='Justice League')

        heroes = [
            User(username='spiderman', email='spiderman@octofit.com', first_name='Peter', last_name='Parker'),
            User(username='ironman', email='ironman@octofit.com', first_name='Tony', last_name='Stark'),
            User(username='batman', email='batman@octofit.com', first_name='Bruce', last_name='Wayne'),
            User(username='superman', email='superman@octofit.com', first_name='Clark', last_name='Kent'),
        ]
        User.objects.bulk_create(heroes)

        users = {user.username: user for user in User.objects.all()}

        Activity.objects.bulk_create(
            [
                Activity(
                    user=users['spiderman'],
                    team=marvel,
                    activity_type='Wall Climb Intervals',
                    duration_minutes=45,
                    calories_burned=420,
                ),
                Activity(
                    user=users['ironman'],
                    team=marvel,
                    activity_type='Repulsor HIIT',
                    duration_minutes=30,
                    calories_burned=360,
                ),
                Activity(
                    user=users['batman'],
                    team=dc,
                    activity_type='Night Sprint',
                    duration_minutes=50,
                    calories_burned=500,
                ),
                Activity(
                    user=users['superman'],
                    team=dc,
                    activity_type='Sky Endurance Flight',
                    duration_minutes=60,
                    calories_burned=650,
                ),
            ]
        )

        Leaderboard.objects.bulk_create(
            [
                Leaderboard(user=users['superman'], rank=1, points=990),
                Leaderboard(user=users['batman'], rank=2, points=910),
                Leaderboard(user=users['spiderman'], rank=3, points=870),
                Leaderboard(user=users['ironman'], rank=4, points=845),
            ]
        )

        Workout.objects.bulk_create(
            [
                Workout(user=users['spiderman'], title='Spider Core Blast', difficulty='Medium', duration_minutes=35),
                Workout(user=users['ironman'], title='Armor Power Circuit', difficulty='Hard', duration_minutes=40),
                Workout(user=users['batman'], title='Bat Cave Strength', difficulty='Hard', duration_minutes=50),
                Workout(user=users['superman'], title='Krypton Endurance', difficulty='Medium', duration_minutes=45),
            ]
        )

        self.stdout.write(self.style.SUCCESS('octofit_db 테스트 데이터 적재 완료'))

from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.routers import DefaultRouter

from .models import Activity, Leaderboard, Team, User, Workout
from .serializers import (
    ActivitySerializer,
    LeaderboardSerializer,
    TeamSerializer,
    UserSerializer,
    WorkoutSerializer,
)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer


class ActivityViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.select_related('user', 'team').all()
    serializer_class = ActivitySerializer


class LeaderboardViewSet(viewsets.ModelViewSet):
    queryset = Leaderboard.objects.select_related('user').all()
    serializer_class = LeaderboardSerializer


class WorkoutViewSet(viewsets.ModelViewSet):
    queryset = Workout.objects.select_related('user').all()
    serializer_class = WorkoutSerializer


router = DefaultRouter()
router.register(r'users', UserViewSet, basename='users')
router.register(r'teams', TeamViewSet, basename='teams')
router.register(r'activities', ActivityViewSet, basename='activities')
router.register(r'leaderboard', LeaderboardViewSet, basename='leaderboard')
router.register(r'workouts', WorkoutViewSet, basename='workouts')


@api_view(['GET'])
def api_root(request, format=None):
    return Response(
        {
            'users': reverse('users-list', request=request, format=format),
            'teams': reverse('teams-list', request=request, format=format),
            'activities': reverse('activities-list', request=request, format=format),
            'leaderboard': reverse('leaderboard-list', request=request, format=format),
            'workouts': reverse('workouts-list', request=request, format=format),
        }
    )

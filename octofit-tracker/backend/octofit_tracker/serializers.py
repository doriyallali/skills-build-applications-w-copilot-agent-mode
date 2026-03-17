from rest_framework import serializers

from .models import Activity, Leaderboard, Team, User, Workout


class ObjectIdStringModelSerializer(serializers.ModelSerializer):
    id = serializers.SerializerMethodField()

    def get_id(self, obj):
        return str(obj.pk)


class UserSerializer(ObjectIdStringModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'joined_at']


class TeamSerializer(ObjectIdStringModelSerializer):
    class Meta:
        model = Team
        fields = ['id', 'name', 'city', 'mascot', 'created_at']


class ActivitySerializer(ObjectIdStringModelSerializer):
    user_id = serializers.SerializerMethodField()
    team_id = serializers.SerializerMethodField()

    class Meta:
        model = Activity
        fields = [
            'id',
            'user_id',
            'team_id',
            'activity_type',
            'duration_minutes',
            'calories_burned',
            'recorded_at',
        ]

    def get_user_id(self, obj):
        return str(obj.user_id)

    def get_team_id(self, obj):
        return str(obj.team_id) if obj.team_id else None


class LeaderboardSerializer(ObjectIdStringModelSerializer):
    user_id = serializers.SerializerMethodField()

    class Meta:
        model = Leaderboard
        fields = ['id', 'user_id', 'points', 'rank', 'updated_at']

    def get_user_id(self, obj):
        return str(obj.user_id)


class WorkoutSerializer(ObjectIdStringModelSerializer):
    user_id = serializers.SerializerMethodField()

    class Meta:
        model = Workout
        fields = ['id', 'user_id', 'title', 'difficulty', 'duration_minutes', 'completed', 'created_at']

    def get_user_id(self, obj):
        return str(obj.user_id)

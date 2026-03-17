from django.contrib import admin

from .models import Activity, Leaderboard, Team, User, Workout


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'joined_at')
    search_fields = ('username', 'email')


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', 'mascot', 'created_at')
    search_fields = ('name', 'city')


@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ('user', 'team', 'activity_type', 'duration_minutes', 'calories_burned', 'recorded_at')
    list_filter = ('activity_type',)


@admin.register(Leaderboard)
class LeaderboardAdmin(admin.ModelAdmin):
    list_display = ('user', 'rank', 'points', 'updated_at')
    ordering = ('rank',)


@admin.register(Workout)
class WorkoutAdmin(admin.ModelAdmin):
    list_display = ('user', 'title', 'difficulty', 'duration_minutes', 'completed', 'created_at')
    list_filter = ('difficulty', 'completed')

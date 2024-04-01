from django.contrib import admin
from .models import University, Gamer, Game, GameEntry, Comment, GameResult


# Register models for administration and customize their display
@admin.register(University)
class UniversityAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Gamer)
class GamerAdmin(admin.ModelAdmin):
    list_display = ('user', 'university', 'description', 'experience')
    list_filter = ('university', 'experience')


class GameResultInline(admin.TabularInline):
    model = GameResult
    extra = 1


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ('name', 'date', 'get_winner_time')
    list_filter = ('winner',)
    inlines = [GameResultInline]

    def get_winner_time(self, obj):
        winner_result = GameResult.objects.filter(game=obj, university=obj.winner).first()
        return winner_result.time_taken if winner_result else None

    get_winner_time.short_description = 'Time taken by winner'


@admin.register(GameEntry)
class GameEntryAdmin(admin.ModelAdmin):
    list_display = ('gamer', 'game')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'game', 'comment_type', 'created_at', 'rating')
    list_filter = ('comment_type', 'created_at')

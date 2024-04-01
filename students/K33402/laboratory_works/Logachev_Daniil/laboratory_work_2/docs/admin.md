```python
from django.contrib import admin
from .models import University, Gamer, Game, GameEntry, Comment, GameResult


# Регистрируем модель University в административном интерфейсе Django и настраиваем отображение списка университетов
@admin.register(University)
class UniversityAdmin(admin.ModelAdmin):
    list_display = ('name',)



# Регистрируем модель Gamer в административном интерфейсе Django и настраиваем отображение списка игроков
@admin.register(Gamer)
class GamerAdmin(admin.ModelAdmin):
    list_display = ('user', 'university', 'description', 'experience')
    list_filter = ('university', 'experience')



# Создаем встроенную форму для отображения результатов игр в административном интерфейсе
class GameResultInline(admin.TabularInline):
    model = GameResult
    extra = 1



# Регистрируем модель Game в административном интерфейсе Django и настраиваем отображение списка игр
@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ('name', 'date', 'get_winner_time')
    list_filter = ('winner',)
    inlines = [GameResultInline]

    # Определяем метод для отображения времени, затраченного победителем игры
    def get_winner_time(self, obj):
        winner_result = GameResult.objects.filter(game=obj, university=obj.winner).first()
        return winner_result.time_taken if winner_result else None

    get_winner_time.short_description = 'Time taken by winner'


# Регистрируем модель GameEntry в административном интерфейсе Django и настраиваем отображение списка участников игр
@admin.register(GameEntry)
class GameEntryAdmin(admin.ModelAdmin):
    list_display = ('gamer', 'game')


# Регистрируем модель Comment в административном интерфейсе Django и настраиваем отображение списка комментариев
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'game', 'comment_type', 'created_at', 'rating')
    list_filter = ('comment_type', 'created_at')

```
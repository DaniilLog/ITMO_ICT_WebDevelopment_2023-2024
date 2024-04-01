from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class University(models.Model):
    # Поле для названия университета с максимальной длиной 100 символов
    name = models.CharField(max_length=100)

    # Отображение названия университета как строкового представления объекта
    def __str__(self):
        return self.name

    # Определение метаданных модели
    class Meta:
        verbose_name = "Университет"  # Единственное название модели в административном интерфейсе
        verbose_name_plural = "Университеты"  # Множественное название модели в административном интерфейсе


# Определение модели Игрок, представляющей отдельных игроков
class Gamer(models.Model):
    # Ассоциация каждого игрока с объектом User в отношении один к одному
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="Пользователь")

    # Позволяет игрокам быть частью команды в отношении многие к одному
    university = models.ForeignKey(University, on_delete=models.SET_NULL, null=True, verbose_name="Университет")

    # Поле для описания игрока
    description = models.TextField(verbose_name="Описание")

    # Поле для опыта игрока, позволяющее оставлять пустые записи
    experience = models.IntegerField(verbose_name="Опыт", null=True, blank=True)

    # Отображение имени пользователя игрока как строкового представления объекта
    def __str__(self):
        return self.user.username

    # Определение метаданных модели
    class Meta:
        verbose_name = "Игрок"  # Единственное название модели в административном интерфейсе
        verbose_name_plural = "Игроки"  # Множественное название модели в административном интерфейсе


# Определение модели Игра, представляющей игровые события
class Game(models.Model):
    # Поле для названия игры с максимальной длиной 100 символов
    name = models.CharField(max_length=100)

    # Поле для даты и времени игры
    date = models.DateTimeField()

    # Позволяет указать победителя игры (команду) в отношении многие к одному
    winner = models.ForeignKey(University, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Победитель")

    # Отображение названия игры как строкового представления объекта
    def __str__(self):
        return self.name

    # Определение метаданных модели
    class Meta:
        verbose_name = "Игра"  # Единственное название модели в административном интерфейсе
        verbose_name_plural = "Игры"  # Множественное название модели в административном интерфейсе


# Определение модели РезультатИгры, представляющей результаты игры
class GameResult(models.Model):
    # Ассоциация каждого результата с определенной игрой в отношении многие к одному
    game = models.ForeignKey(Game, on_delete=models.CASCADE, verbose_name="Игра")

    # Ассоциация каждого результата с определенной командой в отношении многие к одному
    university = models.ForeignKey(University, on_delete=models.CASCADE, verbose_name="Университет")

    # Поле для времени, затраченного командой на прохождение игры
    time_taken = models.DurationField(verbose_name="Время прохождения")

    # Отображение строкового представления объекта результата
    def __str__(self):
        return f"{self.game.name} - {self.university.name} - {self.time_taken}"

    # Определение метаданных модели
    class Meta:
        verbose_name = "Результат игры"  # Единственное название модели в административном интерфейсе
        verbose_name_plural = "Результаты игр"  # Множественное название модели в административном интерфейсе


# Определение модели Участие в игре, представляющей участие игрока в игре
class GameEntry(models.Model):
    # Ассоциация каждой записи с определенным игроком в отношении многие к одному
    gamer = models.ForeignKey(Gamer, on_delete=models.CASCADE, verbose_name="Игрок")

    # Ассоциация каждой записи с определенной игрой в отношении многие к одному
    game = models.ForeignKey(Game, on_delete=models.CASCADE, verbose_name="Игра")

    # Определение метаданных модели
    class Meta:
        verbose_name = "Участие в игре"  # Единственное название модели в административном интерфейсе
        verbose_name_plural = "Участия в играх"  # Множественное название модели в административном интерфейсе


# Определение модели Комментарий, представляющей комментарии пользователей о играх
class Comment(models.Model):
    # Определение вариантов типа комментария
    COMMENT_TYPES = (
        ("cooperation", "Предложения"),  # Предложения
        ("game", "Игры"),  
        ("complaint", "Жалоба"),  # Жалобы
        ("other", "Другое"),  # Другое
    )

    # Ассоциация каждого комментария с определенной игрой в отношении многие к одному
    game = models.ForeignKey(Game, on_delete=models.CASCADE, verbose_name="Игра")

    # Ассоциация каждого комментария с определенным автором (Пользователь) в отношении многие к одному
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Автор")

    # Поле для текстового содержимого комментария
    text = models.TextField(verbose_name="Текст комментария")

    # Поле для типа комментария, используя предопределенные варианты
    comment_type = models.CharField(
        max_length=20,
        choices=COMMENT_TYPES,
        verbose_name="Тип комментария"
    )

    # Поле для рейтинга комментария, проверяющее, что он находится в указанном диапазоне
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(10)],
        verbose_name="Рейтинг"
    )

    # Поле для даты и времени создания комментария, автоматически устанавливается на текущее время
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    # Отображение строкового представления объекта комментария
    def __str__(self):
        return f"{self.author.username} - {self.comment_type} - {self.game.name}"

    # Определение метаданных модели
    class Meta:
        verbose_name = "Комментарий"  # Единственное название модели в административном интерфейсе
        verbose_name_plural = "Комментарии"  # Множественное название модели в административном интерфейсе


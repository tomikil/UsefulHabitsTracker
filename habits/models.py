from django.db import models
from config.settings import AUTH_USER_MODEL

NULLABLE = {"blank": True, "null": True}


class Habit(models.Model):
    NICE_HABIT_CHOICES = (
        (True, 'Приятная'),
        (False, 'Нет')
    )
    PERIODICITY_CHOICES = (
        (True, 'Ежедневная'),
        (False, 'Еженедельная')
    )
    IS_PUBLIC_CHOICES = (
        (True, 'Публичная'),
        (False, 'Приватная')
    )
    owner = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='пользователь')
    place = models.CharField(max_length=150, verbose_name='место')
    time = models.TimeField(verbose_name='время когда выполнить привычку')
    action = models.CharField(max_length=150, verbose_name='действие')
    nice_habit = models.BooleanField(default=True, verbose_name='приятная привычка', choices=NICE_HABIT_CHOICES)
    related = models.ForeignKey('self', on_delete=models.SET_NULL, verbose_name='связанная привычка', **NULLABLE)
    periodicity = models.BooleanField(default=True, verbose_name='периодичность', choices=PERIODICITY_CHOICES)
    prize = models.CharField(max_length=100, verbose_name='вознаграждение', **NULLABLE)
    duration = models.SmallIntegerField(verbose_name='Продолжительность в минутах')
    is_public = models.BooleanField(default=False, verbose_name='признак публичности', choices=IS_PUBLIC_CHOICES)

    def __str__(self):
        return f"Я буду {self.action} в {self.time} в {self.place}"

    class Meta:
        verbose_name = 'привычка'
        verbose_name_plural = 'привычки'
        ordering = ['-id']

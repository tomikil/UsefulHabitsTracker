from rest_framework import serializers


class HabitsValidator:
    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        if value['nice_habit']:
            if value['related'] or value['prize']:
                raise serializers.ValidationError(
                    "Нельзя указать 'приятную привычку' с 'связанной привычкой' или 'вознаграждение'")
            if value['related'] and value['prize']:
                raise serializers.ValidationError(
                    "Нельзя указать 'связанную привычку' и 'вознаграждение'")
            if value['duration'] > 2:
                raise serializers.ValidationError(
                    "Продолжительность выполнения привычки не может быть более 2 минут")
            if value['related']:
                if not value['related'].nice_habit:
                    raise serializers.ValidationError(
                        "Связанная привычка должна быть приятной")

from rest_framework import serializers

from habits.models import Habit
from habits.validators import HabitsValidator


class HabitsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = '__all__'
        validators = [HabitsValidator]

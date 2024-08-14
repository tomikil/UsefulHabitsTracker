from celery import shared_task

from habits.models import Habit
from habits.services import send_telegram_message
import datetime


@shared_task
def send_habit():
    habits = Habit.objects.all()
    current_data = datetime.datetime.now().replace(second=0, microsecond=0).strftime("%X")
    for habit in habits:
        if str(habit.time) == str(current_data):
            tg_chat = habit.owner.tg_chat_id
            message = f"Я буду {habit.action} в {habit.time} в {habit.place}"
            send_telegram_message(tg_chat, message)
            print(tg_chat, message, habit.time, current_data)

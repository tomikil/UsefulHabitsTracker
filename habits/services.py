import requests

from config.settings import TELEGRAM_URL, TELEGRAM_API_KEY


def send_telegram_message(chat_id, message):
    """Отправка сообщения в телеграмм чат"""
    params = {
        'text': message,
        'chat_id': chat_id,
    }
    requests.get(f'{TELEGRAM_URL}{TELEGRAM_API_KEY}/sendMessage', params=params)

from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse

from habits.models import Habit
from users.models import User


class HabitTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(
            email='test@test.ru',
            password='testpassword',
        )
        self.habit = Habit.objects.create(
            place='Дом',
            time='12:00:00',
            action='Выпить стакан воды',
            duration=60,
            periodicity=True,
            owner=self.user,
        )
        self.client.force_authenticate(user=self.user)

    def test_create_habit(self):
        """Тестирование создание привычке"""

        url = reverse("habits:habits_create")
        data = {
            "owner": self.user.pk,
            "place": "Кухня",
            "time": "16:00:00",
            "action": "Помыть посуду",
            "duration": 90,
            "periodicity": True,
        }
        response = self.client.post(url, data)
        data = response.json()

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Habit.objects.all().count(), 2)

    def test_list_habit(self):
        """Тестирование получения списка привычек"""

        url = reverse("habits:habits_list")
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_habit(self):
        """Тестирование получения одной привычки"""

        url = reverse("habits:habits_retrieve", args=(self.habit.pk,))
        response = self.client.get(url)
        data = response.json()

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(data.get('place'), self.habit.place)
        self.assertEqual(data.get('time'), self.habit.time)
        self.assertEqual(data.get('action'), self.habit.action)
        self.assertEqual(data.get('duration'), self.habit.duration)
        self.assertEqual(data.get('periodicity'), self.habit.periodicity)

    def test_update_habit(self):
        """Тестирование изменения привычки"""

        self.url = reverse("habits:habits_update", args=(self.habit.pk,))
        self.data = {
            "duration": 100,
        }
        response = self.client.patch(self.url, data=self.data)
        self.data = response.json()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(self.data["duration"], 100)

    def test_public_habit_list(self):
        """Тестирование получения публичных привычек"""

        url = reverse("habits:habits_public_list")
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_habit(self):
        """Тестирование удаления привычки"""

        url = reverse("habits:habits_destroy", args=(self.habit.pk, ))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Habit.objects.all().count(), 0)

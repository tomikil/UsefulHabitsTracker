from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny

from habits.models import Habit
from habits.paginators import CustomPagination
from habits.serializers import HabitsSerializer
from users.permissions import IsOwner


class HabitsCreateAPIView(generics.CreateAPIView):
    serializer_class = HabitsSerializer
    queryset = Habit.objects.all()
    permission_classes = (IsAuthenticated, IsOwner, )

    def perform_create(self, serializer):
        habit = serializer.save()
        habit.owner = self.request.user
        habit.save()


class HabitsListAPIView(generics.ListAPIView):
    serializer_class = HabitsSerializer
    queryset = Habit.objects.all()
    permission_classes = (IsAuthenticated, )
    pagination_class = CustomPagination

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(owner=self.request.user)


class HabitsRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = HabitsSerializer
    queryset = Habit.objects.all()
    permission_classes = (IsAuthenticated, IsOwner, )


class HabitsUpdateAPIView(generics.UpdateAPIView):
    serializer_class = HabitsSerializer
    queryset = Habit.objects.all()
    permission_classes = (IsAuthenticated, IsOwner, )


class HabitsDestroyAPIView(generics.DestroyAPIView):
    serializer_class = HabitsSerializer
    queryset = Habit.objects.all()
    permission_classes = (IsAuthenticated, IsOwner, )


class HabitsPublicListAPIView(generics.ListAPIView):
    serializer_class = HabitsSerializer
    queryset = Habit.objects.filter(is_public=True)
    permission_classes = (AllowAny, )
    pagination_class = CustomPagination

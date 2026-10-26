from datetime import date, timedelta

from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated

from .serializers import SignupSerializer, ExpenseSerializer
from .models import Expense


class SignupView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = SignupSerializer
    permission_classes = [AllowAny]


class ExpenseListCreateView(generics.ListCreateAPIView):
    serializer_class = ExpenseSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Expense.objects.filter(
            user=self.request.user
        ).order_by('-date')

        period = self.request.query_params.get('period')
        today = date.today()

        if period == 'week':
            start_date = today - timedelta(days=6)
            queryset = queryset.filter(date__range=[start_date, today])

        elif period == 'month':
            start_date = today.replace(day=1)
            queryset = queryset.filter(date__range=[start_date, today])

        elif period == '3months':
            start_date = today - timedelta(days=89)
            queryset = queryset.filter(date__range=[start_date, today])

        start = self.request.query_params.get('start_date')
        end = self.request.query_params.get('end_date')

        if start:
            queryset = queryset.filter(date__gte=start)

        if end:
            queryset = queryset.filter(date__lte=end)

        return queryset

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ExpenseDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ExpenseSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Expense.objects.filter(user=self.request.user)
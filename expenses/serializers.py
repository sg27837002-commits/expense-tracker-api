
from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Expense


class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expense
        fields = [
            'id',
            'title',
            'amount',
            'category',
            'description',
            'date',
            'created_at',
        ]
        read_only_fields = ['id', 'created_at']


class SignupSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True,
        min_length=8
    )

    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'email',
            'password',
        ]
        read_only_fields = ['id']

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

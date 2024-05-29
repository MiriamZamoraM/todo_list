from rest_framework import serializers
from .models import Task
from users.models import User

class TaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = ("id", "name", "status", "created", "limit", "user_id")
        read_only_fields = ("created",)

    def create(self, validated_data):
        model = self.Meta.model
        name = validated_data.get("name")
        status = validated_data.get("status")
        limit = validated_data.get("limit")
        user_id = validated_data.get("user_id")

        task = model.objects.create(**validated_data)
        task.save()
        return task
    
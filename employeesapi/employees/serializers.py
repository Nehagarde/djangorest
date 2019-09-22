from rest_framework import serializers
from . models import Employees


class EmployeeSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=250)
    email = serializers.EmailField()

    def create(self, validated_data):
        return Employees.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', instance.email)

        instance.save()
        return instance
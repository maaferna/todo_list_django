from rest_framework import serializers
from .models import Task
from django.contrib.auth.models import User

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

    def to_representation(self, instance):
        rep = super(UserSerializer, self).to_representation(instance)
        rep['username'] = str(instance.username)
        return rep

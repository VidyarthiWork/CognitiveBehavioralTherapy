from rest_framework import serializers
from .models import CognitiveModel


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CognitiveModel
        fields = ('id', 'text')

    def create(self, validated_data):
        # print("id: " + validated_data["id"])
        print("text: " + validated_data["text"])
        return super(TodoSerializer, self).create(validated_data)

    def update(self, instance, validated_data):
        # print("id: " + instance.id)
        print("text: " + instance.text)
        return super(TodoSerializer, self).update(instance, validated_data)

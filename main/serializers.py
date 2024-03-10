from rest_framework import serializers
from .models import ConversationTopic, ConversationMessage

class ConvTopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConversationTopic
        fields = '__all__'

class ConvMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConversationMessage
        fields = '__all__'

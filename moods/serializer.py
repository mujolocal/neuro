from .models import Mood
from rest_framework import serializers

class MoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mood
        fields = '__all__' 
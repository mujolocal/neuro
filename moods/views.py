from rest_framework import generics
from .models import Mood
from .serializer import MoodSerializer

class MoodListViewset(generics.ListCreateAPIView):
    queryset = Mood.objects.all()
    serializer_class = MoodSerializer
    

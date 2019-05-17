from rest_framework import generics
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import Mood
from .serializer import MoodSerializer


class MoodListViewset(generics.ListCreateAPIView):
    queryset = Mood.objects.filter(person=1)
    serializer_class = MoodSerializer
    def get_queryset(self):
        user = self.request.user
        print(type(user.pk))
        if isinstance(user.pk,int):
            return  Mood.objects.filter(person=user)
        else:
            return None
    
    

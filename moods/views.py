from rest_framework import generics
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import Mood
from .serializer import MoodSerializer
from datetime import date
from django.contrib.auth.models import User
import math 
from django.shortcuts import render


class MoodCreateViewset(generics.CreateAPIView):
    serializer_class = MoodSerializer
    users  = User.objects.all()
    
    def get_queryset(self):
        user = self.request.user
        # print(type(user.pk))
        
        if isinstance(user.pk,int):
            return  Mood.objects.filter(person=user)
        else:
            return None
            
    def perform_create(self, serializer):
        user = self.request.user
        moods =  Mood.objects.filter(person=user)
        lastmood = moods[len(moods)-1]
        if abs((date.today() - lastmood.created ).days) == 0 and len(moods)>0:
            serializer.save(streak = lastmood.streak)  
        elif abs((date.today() - lastmood.created ).days) == 1 and len(moods)>0:
            serializer.save(streak = 1)
        else:
            serializer.save(streak = lastmood.streak+1)  
            
def list_percent_view(request):
    user = request.user
    latest_streaks = getlateststreak()
    cutoff = fifty_percent(latest_streaks)
    if isinstance(user.pk,int):
        moods =  Mood.objects.filter(person=user.pk)
        print(moods)
        # show_score = 
        html_dict = {
        "moods":moods,
        "show_score":True if latest_streaks[user.username] >= cutoff else False,
        "score":percentage(number=latest_streaks[user.username] ,num_list=list(latest_streaks.values())),
        "latest_streak":latest_streaks[user.username]
        }
        return  render(request, "moods/listperc.html" , html_dict)
    else:
        return render(request, "moods/listperc.html")
    
    

def getlateststreak():
    user_numbers = [user.pk for user in User.objects.all() ]
    user_names = [user.username for user in User.objects.all() ]
    score_dict = {}
    for i in range(len(user_names)):
        person_moods = Mood.objects.filter(person=user_numbers[i])
        score_dict[user_names[i]] = person_moods[len(person_moods)-1].streak
        
    return score_dict

def fifty_percent(streak_dict:dict):
    values = list(streak_dict.values())
    print(values)
    # values = streak_dict.values().sort()
    halfsize = math.ceil(len(values)/2)
    print(values[halfsize])
    return values[halfsize]
    
def percentage(number, num_list):
    num_list.sort()
    return (num_list.index(number)+1)/len(num_list)*100
            
    
    

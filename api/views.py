from django.shortcuts import render
from django.http import JsonResponse
from .models import Profile
from .serializers import ProfileSerializer


def profile_list(request):
    info = Profile.objects.all()
    serializer =  ProfileSerializer(info, many=True)
    return JsonResponse(serializer.data, safe=False )  
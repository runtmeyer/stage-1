from rest_framework import serializers
from .models import Input

#class ProfileSerializer(serializers.ModelSerializer):
    #class Meta:
        #model = Profile
        #fields = ['slackUsername', 'backend', 'age', 'bio'] 

class InputSerializer(serializers.ModelSerializer):
    class Meta:
        model = Input
        fields = ['operation_type', 'x', 'y']
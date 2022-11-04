from django.shortcuts import render 
from django.http import JsonResponse
from .models import Input


from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import InputSerializer


#def profile_list(request):
    #info = Profile.objects.all()
    #serializer =  ProfileSerializer(info, many=True)
    #return JsonResponse(serializer.data[0], safe=False )  


@api_view(['POST', 'GET']) 
def test3(request):
    serializer = InputSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save() 

    operation = Input.objects.all()
    serializer = InputSerializer(operation, many=True)
    choice = serializer.data[-1]["operation_type"]  
   

    def res():
        num1 = serializer.data[-1]["x"]
        num2 = serializer.data[-1]["y"] 

        add = num1 + num2
        sub = num1 - num2
        mul = num1 * num2 

        if choice == "addition":
            result = add
        elif choice == "subtraction":
            result = sub
        elif choice == "multiplication":
            result = mul

        return result 

     

    #def finalanswer():
        #answer = ({"slackUsername": "muobotone", "result": anser, "operation_type" : choice})

        #return answer


    #return Response(answer)

    anser = res()
    return Response({"slackUsername": "muobotone", "result": anser, "operation_type" : choice}) 

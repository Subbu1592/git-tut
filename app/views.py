from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer
from django.http import HttpResponse

# Create your views here.
#def home(request): this we use to render templates(home.html)
#    return render(request, 'home.html)





#POST- methode is used to add data
#GET- methode is used to get(retrive) data
#PUT- method is used to update data
#PATCH- method is used to partially update data
#DELETE= method is used to delete data



@api_view(['GET','POST','PATCH','DELETE','PUT']) #here im calling only GET method if i leave it blank it will call all methods
def home(request):
    if request.method =='GET':
   
        return Response({
            'message':'you called GET method',
            'status':400
            })

    elif request.method == 'POST':
        return Response({
            'message':'here we called POST method',
            'status':400,

            })

    elif request.method == 'PATCH':
        return Response({
            'message':'here we called PATCH method',
            'status':400,

            })

    elif request.method == 'PUT':
        return Response({
            'message':'here we called PUT method',
            'status':400,

            })


    elif request.method == 'DELETE':
        return Response({
            'message':'here we called DELETE method',
            'status':400,

            })


    else:
        return Response({
            'message':'here we called Invalid method',
            'status':404,

            })
#serializer = serializers.TemperatureSerializer(data=request.data,
#context={'request': request})



@api_view(['POST'])   # POST meth0d for student model
def post_student(request):
    try:
        data = request.data
        serializer = StudentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({
            'message':'valid function',
            'status':True,
            'data':serializer.data

            })
        
        return Response({
            'message':'invalid student',
            'status':False,
            'data':serializer.errors

                })

    except Exception as e:
        print (e)
    return Response({
            'message':'Invalid function',
            'status':False,

            })




@api_view(['GET'])  #GET method for student model
def get_student(request):
    data= Student.objects.all()
    serializer= StudentSerializer(data, many=True)
    

    return Response({
            'message':'GET function called',
            'status':True,
            'data':serializer.data

            })
    
    
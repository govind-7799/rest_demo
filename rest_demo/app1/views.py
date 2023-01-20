from django.shortcuts import render
from rest_framework.decorators import api_view,permission_classes
from .models import Dummydata
from .serializers import dummyserilizer
from rest_framework.response import Response
from rest_framework import status
from django.core.exceptions import ObjectDoesNotExist
import requests
import json
from rest_framework.permissions import IsAuthenticated

@api_view(['GET','POST'])
@permission_classes([IsAuthenticated])
def showdata(request):
    content={
        'status':'access denied'
    }
    
    if request.method=='GET':
        data=Dummydata.objects.all()
        serilizer=dummyserilizer(data, many=True)
        return Response(serilizer.data,content)

    elif request.method=='POST':
        serilizer=dummyserilizer(data=request.data)
        if serilizer.is_valid():
            serilizer.save()
            return Response(serilizer.data,status=status.HTTP_200_OK)
        return Response(serilizer.errors,status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET','PUT','DELETE'])
def showdetails(request,pk):
    try:
        snippet=Dummydata.objects.get(pk=pk)
    except ObjectDoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method=='GET':
        
        serilizer=dummyserilizer(snippet)
        return Response(serilizer.data)
    elif request.method=='PUT':
        serilizer=dummyserilizer(snippet,data=request.data)
        if serilizer.is_valid():
            serilizer.save()
            return Response(serilizer.data)
        return Response(serilizer.errors,status=status.HTTP_400_BAD_REQUEST)
    elif request.method=='DELETE':
        serilizer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

def demodata(request):
    response=requests.get("http://127.0.0.1:8000/one").json()
    return render(request,'demo.html',{'response':response})
    




       




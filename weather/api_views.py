from rest_framework import status
from .models import City
from .serializers import CitySerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view

status_200 = status.HTTP_200_OK
status_400 = status.HTTP_400_BAD_REQUEST

@api_view(['GET'])
def getAllCities(request):
    try:
        city = City.objects.all()
        city_serializer = CitySerializer(city, many = True)
        cities = city_serializer.data

        return Response({
            "data": {
                "status": status_200,
                "cities": cities
            },
        })
        
    except Exception as e:
        return Response({
            'data': {
                'status': status_400,
                'error': str(e)
                },
            })

@api_view(['GET'])
def getCity(request , id):
    try:
        city = City.objects.get(id=id)
        city_serializer = CitySerializer(city)
        cities = city_serializer.data

        return Response({
            "data": {
                "status": status_200,
                "cities": cities
            },
        })
        
    except Exception as e:
        return Response({
            'data': {
                'status': status_400,
                'error': str(e)
                },
            })

@api_view(['POST'])
def addCity(request):
    try:
        city = request.data['city']
        if city == "":  
            return Response({
                "data": {
                "status": status_400,
                "error":"Enter City Name"
            },
            })
        else:
            obj = City(city=city)
            obj.save()

        return Response({
                "data": {
                    "status": status_200,
                    "success":"City Added Successfully"
                },
            })
    
    except Exception as e:
        return Response({
            'data': {
                'status': status_400,
                'error': str(e)
                },
            })

@api_view(['PUT'])
def CityUpdate(request,id):
    try:
        city = City.objects.get(pk=id)
        serializer = CitySerializer(instance=city, data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response({
                "data": {
                    "status": status_200,
                    "success":"City Updated Successfully",
                    "city": serializer.data
                },
            })

    except Exception as e:
        return Response({
            'data': {
                'status': status_400,
                'error': str(e)
                },
            })

@api_view(['DELETE'])
def cityDelete(request,id):
    try:
        city = City.objects.get(id=id)
        city.delete()
        return Response({
            "data": {
                "status": status_200,
                "success":"City Deleted Successfully"
            },
        })
        
    except Exception as e:
        return Response({
            'data': {
                'status': status_400,
                'error': str(e)
                },
            })
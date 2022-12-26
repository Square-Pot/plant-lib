from django.contrib.auth.models import User, Group
from library.models import Plant
from rest_framework import viewsets
from rest_framework import permissions
from PlantLib.api.serializers import UserSerializer, GroupSerializer, PlantSerializer

# parsing data from the client
from rest_framework.parsers import JSONParser
# To bypass having a CSRF token
from django.views.decorators.csrf import csrf_exempt
# for sending response to the client
from django.http import HttpResponse, JsonResponse
# API definition for task
from .serializers import PlantSerializer
# Task model
from library.models import Plant



class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class PlantsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows plants to be viewed or edited.
    """
    queryset = Plant.objects.all()
    serializer_class = PlantSerializer
    permission_classes = [permissions.IsAuthenticated]


@csrf_exempt
def plants(request):
    '''
    List all plant snippets
    '''
    if(request.method == 'GET'):
        # get all the plants
        plants = Plant.objects.all()
        # serialize the task data
        serializer = PlantSerializer(plants, many=True)
        # return a Json response
        return JsonResponse(serializer.data,safe=False)
    elif(request.method == 'POST'):
        # parse the incoming information
        data = JSONParser().parse(request)
        # instanciate with the serializer
        serializer = PlantSerializer(data=data)
        # check if the sent information is okay
        if(serializer.is_valid()):
            # if okay, save it on the database
            serializer.save()
            # provide a Json Response with the data that was saved
            return JsonResponse(serializer.data, status=201)
            # provide a Json Response with the necessary error information
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def get_plant_by_uid(request, uid=None):
    
    if(request.method == 'GET'):
        # get all the plants
        plant = Plant.objects.get(uid=uid)
        # serialize the task data
        serializer = PlantSerializer(plant, many=False)
        # return a Json response
        return JsonResponse(serializer.data, safe=False)



# @csrf_exempt
# def edit_plant(request, uid):
#     try:
#         # obtain the task with the passed id.
#         task = Plant.objects.get(uid=uid)
#     except:
#         # respond with a 404 error message
#         return HttpResponse(status=404)  
#     if(request.method == 'PUT'):
#         # parse the incoming information
#         data = JSONParser().parse(request)  
#         # instanciate with the serializer
#         serializer = PlantSerializer(task, data=data)
#         # check whether the sent information is okay
#         if(serializer.is_valid()):  
#             # if okay, save it on the database
#             serializer.save() 
#             # provide a JSON response with the data that was submitted
#             return JsonResponse(serializer.data, status=201)
#         # provide a JSON response with the necessary error information
#         return JsonResponse(serializer.errors, status=400)
#     elif(request.method == 'DELETE'):
#         # delete the task
#         Plant.delete() 
#         # return a no content response.
#         return HttpResponse(status=204) 
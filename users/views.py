from django.contrib.auth import get_user_model
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from users.serializers import CustomUserRegisterSerializer
# Create your views here.

class CustomUserRegisterView(generics.CreateAPIView):
    # in settings.py of backend project we have configured custom user model to be used globally and this is how we should be importing it.
    model = get_user_model()
    serializer_class = CustomUserRegisterSerializer
    
    # allow any user to call this api
    permission_classes= [
        permissions.AllowAny
    ]

    # this ensures that we are not sending back the same user object on successfull creation to secure user data
    def create(self,request, *args,**kwargs):
        super().create(request, *args, **kwargs)
        return Response(status=status.HTTP_201_CREATED)
    


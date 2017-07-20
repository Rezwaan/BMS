from django.shortcuts import render

# Create your views here.

from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

from django.contrib.auth.models import User
from models import UserDetails
from credential.serializer import UserLoginSerializer,UserSerializer,UserDetailsSerializer,UserLoginIDSerializer,friendEmailSerilizer

from rest_framework.permissions import IsAuthenticated
from django.core.mail import send_mail
from django.conf import settings

@permission_classes((IsAuthenticated,))
@api_view(['GET', 'POST'])
def user_list(request):
    """
    List all users, or create a new user.
    """
    if request.method == 'GET':
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():

            user = User(username=serializer.validated_data['username'],email=serializer.validated_data['email'],first_name=serializer.validated_data['first_name'],last_name=serializer.validated_data['last_name'])
            user.set_password(raw_password=serializer.validated_data['password'])
            user.save()
            subject="Confirmation Email"
            message="Thanks for signing-up with SHOPNROAR"
            to_list=[user.email]
            from_email=settings.EMAIL_HOST_USER
            send_mail(subject,message,from_email,to_list,fail_silently=True)

           # serializer.validated_data['password'] = User.set_password(serializer.validated_data['password'])
            #serializer.save()
            serializer = UserSerializer(user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST)





@api_view(['POST'])
def user_login(request):
   #usercred= serializers();

    json = {}
    u = User()
    serializer =UserLoginSerializer(u, data=request.data)
    if serializer.is_valid():
        try:
            user = User.objects.get(email=serializer.validated_data['email'])
            if request.method == 'POST':
                if user.validate_password(serializer.validated_data['password']):

                    return Response(serializer.data, status=status.HTTP_200_OK)
                else:
                    json['message'] = 'success'
                    return Response(json['message'], status=status.HTTP_406_NOT_ACCEPTABLE)
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    else:
        return Response(
            serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])

def getID(request,query):
    try:


        Mobile_all = User.objects.filter(username__icontains=query)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


    if request.method == 'GET':
        serializer = UserLoginIDSerializer(Mobile_all, many=True)  # many=True so it doesn't return only 1 JSON Object
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)

    pass


@api_view(['GET', 'POST'])
def userDetaillist(request):
    if request.method == 'GET':
        customers = UserDetails.objects.all()
        serializer = UserDetailsSerializer(customers, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':

        serializer = UserDetailsSerializer(data=request.data)
        if serializer.is_valid():
            # user = User(user_id=serializer.validated_data['id'],Mobile=serializer.validated_data['Mobile'],email=serializer.validated_data['email'],newsLetter=serializer.validated_data['newsLetter'])

            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




@api_view(['POST'])
def emailToFriend(request):

    if request.method == 'POST':

        serializer = friendEmailSerilizer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            # subject="Your friend share this page with you"
            # message="here you can visit our page by clicking on this link "+friendEmailSerilizer.sharedlink
            # to_list=[friendEmailSerilizer.email]
            # from_email=settings.EMAIL_HOST_USER
            # send_mail(subject,message,from_email,to_list,fail_silently=True)


            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
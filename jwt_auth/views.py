from django.shortcuts import render, redirect

from .serializers import UserSerializer
from django.conf import settings
from  authlib.integrations.django_client import OAuth
from django.http import HttpResponse
from .models import User
from rest_framework.decorators import api_view
import os

client_id = os.environ.get('google_client_id')
client_secret = os.environ.get('google_secret_id')

SCOPES =['email','profile']


oauth = OAuth()

CONF_URL='https://accounts.google.com/.well-known/openid-configuration'
oauth.register(
    
    name= 'google',
    server_metadata_url=CONF_URL,

    client_id= client_id,
    client_secret=client_secret,
    access_token_url= 'https://oauth2.googleapis.com/token',
    authorize_url= 'https://accounts.google.com/o/oauth2/v2/auth',
    api_base_url='www.googleapis.com',
    client_kwargs={
            'scope':'email profile',
            'state':'random_string',
    
    }



)

def check_user_db(data):
    user = User.objects.get(email=data['email'])

    #  check is password matches 

    print(user)


@api_view(['POST'])

def signup(request):

    serializer = UserSerializer(data=request.data)


    # 1. validate the incoming data

    if serializer.is_valid():

        # 2. create a new user  in the database
            serializer.save()

            return HttpResponse({"message":"user created successfully"})
    else:
        return HttpResponse({"messagee":"invalid data"})



@api_view(['POST'])        

def signin(request):

    #  valid  incoming data 
    serializer = UserSerializer(data=request.data)

    if serializer.is_valid():
            # check if  user exists in the database
            check_user_db(serializer.data)


    return HttpResponse("signin called")



def signin_google(request):
    google = oauth.create_client('google')

    google = oauth.google
    redirect_uri = f'http://127.0.0.1:8000/jwtauth/homepage'


    return google.authorize_redirect(request,redirect_uri)




def signup_google(request):

    pass





def logout(request):

    pass





def homepage(request):

    google = oauth.create_client('google')
    token = oauth.google.authorize_access_token(request)

    user_data = google.get('https://www.googleapis.com/oauth2/v2/userinfo',token=token)

    user = user_data.json()


    return redirect('http://127.0.0.1:8000/jwtauth/callback/')



def callback(request):

    
    return HttpResponse("callback")


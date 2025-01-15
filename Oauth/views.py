from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
import requests
import requests.compat

authorize_url= 'https://github.com/login/oauth/authorize'
def github_login(request):

    params= {

       
        'client_id':'',
        'scope':'user:email',
        'state':'random_string',
         
    } 

    url = f"{authorize_url}?{requests.compat.urlencode(params)}"

    return redirect(url)




def github_callback(request):

    code = request.GET.get('code')


    if not code:
        print("not code")

    token_data={

    'client_id':"",
    'client_secret':"",
    'code':code,
    'scope':'user:email'

    }

    header = {
        'Accept':'application/json'
    }

    token_reponse = requests.post('https://github.com/login/oauth/access_token',data=token_data,headers=header)

    if token_reponse.status_code!=200:
        return "you need to first authenticate"

    #  fetch user information through access token

    token = token_reponse.json()
    #  in case access_token got expired then referesh token

    if token.get('error'):



        return HttpResponse("you need to first login")
      

    access_token = token.get('access_token')
    #  fetch user information through access token


    user_resp = requests.get('https://api.github.com/user',headers={

        'Authorization':'Bearer '+access_token,
        'Accept':'application/json'
    })
    

    user = user_resp.json()
    print(user)
    return HttpResponse("callback called")



def logout(request):

    #  clear session
    pass

    #  redirect to login page

    

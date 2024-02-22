from django.http import JsonResponse
from django.shortcuts import render, redirect
from .forms import *
from .utils import *
from .embed import *
import threading
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view

def index(request):
    
    if request.POST:
        uid = request.POST.get('uid')
        prompt = request.POST.get('prompt')
        print(prompt,uid)
        
        emb = Emmbedded(uid=uid, prompt=prompt)
        responce = emb.query()
        print(responce)
        
    return render(request,'chatbot/chat.html',{})


def college_form(request):
    if request.method == 'POST':
        form = CollegeForm(request.POST)
        if form.is_valid():
            mid = form.save()
            root_url = form.cleaned_data['root_url']
            
            start_page_source(mid.id, root_url)
            
            return redirect('index')  
    else:
        form = CollegeForm()
    return render(request, 'chatbot/college.html', {'form': form})

@csrf_exempt
@api_view(['POST'])
def get_chat_responce(request):
    responce = {
        "status": 403,
        "request" : "",
        "response" :"",
        "updated":"",
        "profile_url":"",
        "name":"",
        "time":"",
        "error":False
    }
    
    if request.method == 'POST':
        uid = request.POST.get('uuid')
        query = request.POST.get('query')
        print("UUID : ",uid)
        print("QUERY : ",query)
        clg = College.objects.get(uid=uid)
        print(clg.name)
        responce['name'] = clg.name
        responce['profile_url'] = clg.logo
        print(responce['profile_url'])
        responce['updated'] = clg.updated.date()
        try:
            obj = Emmbedded(uid=uid,prompt=query)
            responce['response'] = obj.query()
            msg = Messages(to=clg,request=query,responce=responce['response'])
            msg.save()
            responce['time'] = msg.created.time()
            responce['status'] = 200
        except Exception as e:
            responce['response'] = str(e)
            responce['error'] = True
        
        
    return JsonResponse(responce)

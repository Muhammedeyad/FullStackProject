from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.middleware.csrf import get_token

from rest_framework.decorators import api_view #unwanted thing i never used inthis project
import json
# Create your views here.

def index(request):
    return render(request, 'index.html')
    
    
def btnData(request): 
    bodyunicode = request.body.decode('utf-8')
    data = json.loads(bodyunicode)
    return JsonResponse({'status':'data receiced succesfully', 'data': data})

def get_csrf_token(request):
    csrf_token = get_token(request)
    return JsonResponse({'csrfToken': csrf_token})
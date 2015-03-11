from django.shortcuts import render, render_to_response
from django.http import HttpResponse
import json
from django.core import serializers
# Create your views here.

def login(request, userid, password):
	data = {}
	data['userid']=userid
	data['password']=password
	data['token']="token_value"
	return HttpResponse(json.dumps(data), content_type="application/json")

def tasks_json(request):
    tasks = Task.objects.all()
    data = serializers.serialize("json", tasks)
    return HttpResponse(data, content_type='application/json')	

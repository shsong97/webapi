from django.shortcuts import render, render_to_response
from django.http import HttpResponse
import json
from django.core import serializers
from django.contrib.auth.models import User
# Create your views here.

def login(request, userid, password):
	data = {}
	data['userid']=userid
	data['password']=password
	data['token']="token_value"
	return HttpResponse(json.dumps(data), content_type="application/json")

def user_list(request):
    userlist = User.objects.all()
    data = serializers.serialize("json", userlist)
    return HttpResponse(data, content_type='application/json')	

def perm(request, systemid, userid):
	data = {}
	data['userid']=userid
	data['systemid']=systemid
	data['token']="token_value"
	data['programid']=["program1","program2","program3"]
	
	return HttpResponse(json.dumps(data), content_type="application/json")
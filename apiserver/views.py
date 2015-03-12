from django.shortcuts import render, render_to_response
from django.http import HttpResponse
import json
from django.core import serializers
from django.contrib.auth.models import User
import hashlib, binascii
import os
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

SALT=os.urandom(16) # This function returns random bytes from an OS-specific randomness source

def enc_pass(password):	
	dk1 = hashlib.pbkdf2_hmac('sha256', password, SALT, 100000)
	return binascii.hexlify(dk1)

def login(request, userid, password):
	data = {}
	data['userid']=userid
	data['token']=enc_pass(password)
	return HttpResponse(json.dumps(data), content_type="application/json")

def user_list(request):
    userlist = User.objects.all()
    data = serializers.serialize("json", userlist)
    return HttpResponse(data, content_type='application/json')	

#@csrf_exempt
def perm(request, systemid, userid, token):
	enc_password=enc_pass("d")
	
	data = {}
	data['programid']=[]
	if enc_password == token:
		arglist=[]
		for arg in range(10):
			arglist.append(systemid+"_program_"+str(arg))
		data['programid']=arglist

	return HttpResponse(json.dumps(data), content_type="application/json")


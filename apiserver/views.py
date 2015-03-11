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
	
def login(request, userid, password):
	data = {}
	data['userid']=userid
	data['password']=password
	dk = hashlib.pbkdf2_hmac('sha256', password, SALT, 100000)
	data['token']=binascii.hexlify(dk)
	return HttpResponse(json.dumps(data), content_type="application/json")

def user_list(request):
    userlist = User.objects.all()
    data = serializers.serialize("json", userlist)
    return HttpResponse(data, content_type='application/json')	

@csrf_exempt
def perm(request, systemid, userid):
	data = {}
	data['userid']=userid
	data['systemid']=systemid
	data['token']="token_value"
	
	password="aaa"
	dk1 = hashlib.pbkdf2_hmac('sha256', password, SALT, 100000)
	enc_password=binascii.hexlify(dk1)
	
	req_token=json.loads(request.body)
	
	dk2 = hashlib.pbkdf2_hmac('sha256', req_token['password'], SALT, 100000)
	req_password=binascii.hexlify(dk2)
	
	if enc_password == req_password:
		valid=True
		data['valid']='true'
	else:
		valid=False
		data['valid']='false'

	arglist=[]
	data['programid']=[]
	if valid:
		for arg in range(10):
			arglist.append(systemid+"_program_"+str(arg))
		data['programid']=arglist

	return HttpResponse(json.dumps(data), content_type="application/json")
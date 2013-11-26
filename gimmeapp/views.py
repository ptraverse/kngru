from django.core.context_processors import csrf
from django.shortcuts import render_to_response
from django.shortcuts import render
from django.shortcuts import HttpResponseRedirect
from gimmeapp.models import Post
from gimmeapp.models import Comment
from gimmeapp.models import Like
from gimmeapp.models import Lottery
from django.template import RequestContext
from gimmeapp.models import Userg
from gimmeapp.models import Target
from gimmeapp.models import *
from datetime import datetime    
from django.http import *
from gimmeapp.forms import PostForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.utils import simplejson
import socket
import bitly_api
import sys


def target(request):
	return render(request, "target.html" )

def view_target(request, short):
	t = Target.objects.get(short=short)
	return render(request, "view_target.html", {"target":t} )

def create_target_json(request):
	if request.POST.has_key('client_response'):
		API_USER = "cfd992841301aabcd843e8ed4622b9c88e320e8e"
		API_KEY = "c5955c440b750b215924bd08d1b79518ca4a82c4"
		ACCESS_TOKEN = "1214d30c74adf88608b83bdc8eac7b053a57b6f4" 
		b = bitly_api.Connection(access_token=ACCESS_TOKEN)
		x = request.POST.get('client_response','')                 
		y = b.shorten(uri=x)                         
		response_dict = {}                                         
		response_dict.update({'server_response': y })                                                                  
		return HttpResponse(simplejson.dumps(response_dict), mimetype='application/javascript')
	#else:
		#return render_to_response('target', context_instance=RequestContext(request))

def create_target2(request):
	if request.method == 'POST':
		API_USER = "cfd992841301aabcd843e8ed4622b9c88e320e8e"
		API_KEY = "c5955c440b750b215924bd08d1b79518ca4a82c4"
		ACCESS_TOKEN = "1214d30c74adf88608b83bdc8eac7b053a57b6f4" 
		b = bitly_api.Connection(access_token=ACCESS_TOKEN)
		long_url = request.POST.get("element_url","")
		response = b.shorten(uri=long_url)
		response_url = response['url']
		return render(request, "confirm2.html", { "response":response } ) 


def create_target(request):
	if request.method == 'POST': # If the form has been submitted...
		t = Target.objects.create()
		#t.User_created = request.user
		req_use = request.user
		t.User_created_id = req_use.id	
		#req_userg = request.user
		#p.userg_created_id = req_userg.id
		#p.user_auth_created = request.user
		t.url = request.POST.get("element_url","")
		element_short = request.POST.get("element_short","")
		if element_short=='':
			t.determine_short()
		else:
			exists_already = t.check(element_short)
			if (exists_already):
				return render_to_response('../target/', { "exists_already":True, "previous_short":element_short } )
			else:
				t.short = element_short
		t.PPCContract = request.POST.get("element_partipate","")
		t.date_created = datetime.now()
		t.save()
		return render_to_response("confirm.html", {"target_created":t} )
	else:
		return HttpResponseRedirect('preforms/form/e404_page.html')


def user_home(request):
	return render(request, "user_home.html" )

def user_friends(request):
	return render(request, "user_friends.html" )

def user_receipts(request):
	return render(request, "user_receipts.html" )

def user_edit(request):
	return render(request, "user_edit.html" )

def log_in(request):
	if request.method=='POST':
		username = request.POST.get("username","")
		password = request.POST.get("password","")
		user = authenticate(username=username, password=password)
		if user is not None:
      	 		if user.is_active:
      	 			login(request, user)
				return HttpResponseRedirect('../allposts' )	
	       	else:
			return HttpResponseRedirect('../sign-up')
	else:
		return render(request,'login.html' )
#def log_in(request): 
			
def log_out(request):
	logout(request)
	return HttpResponseRedirect('../')

def landing_page(request):
	return render(request, 'preforms/form/landing_page.html' )

def e404_page(request, othertext):
	return render_to_response('preforms/form/e404_page.html' )

def preform(request):
	return render_to_response('preforms/form/form.html' )

def new_post_form(request):
	return render(request,'preforms/form/new_post_form.html' )

def create_post(request):
	if request.method == 'POST': # If the form has been submitted...
		p = Post.objects.create()
		p.user_created = request.POST.get("element_1","")	
		req_userg = request.user
		p.userg_created_id = req_userg.id
		p.user_auth_created = request.user
		p.name = request.POST.get("element_2","")
		p.description = request.POST.get("element_3","")
		p.url = request.POST.get("element_url","")
		h = Post_Hash.objects.create(post=p, hash=p.create_hash())
		#try:
		#	h.hash = h.get_hash()
		#except IntegrityError:
		#	h.hash = "error" 
		h.save()
		p.save()
        	postlist = Post.objects.all()
		return HttpResponseRedirect('../allposts')
	else:
		return HttpResponseRedirect('../new-post')
	
def sign_up(request):
	if request.method=='POST':
		email = request.POST.get("element_1","")
		password = request.POST.get("element_3","")
		u = User.objects.create_user(email,email,password)
		ug = Userg.objects.create(user_id = u.id, name=email, date_created = datetime.now() , current_points=0, cash = 0, point_multiplier = 1 )
		return HttpResponseRedirect('../allposts')
	else:
		return render(request,'preforms/form/sign_up_form.html' )

def view_post(request,post_hash):
	ph = Post_Hash.objects.get(hash=post_hash)
	p = ph.post
	return render_to_response('post.html', {  "post":p , "hash":post_hash } )

def url_redirect(request,post_hash):
	ph = Post_Hash.objects.get(hash=post_hash)
	p = ph.post
	# TODO add a bunch of logic here
	return HttpResponseRedirect(p.url)

def view_all_posts(request):
	postlist = Post.objects.all()	
	if (len(postlist)==0):
		p = Post.objects.create(name="primo")
		p.save()
		postlist = [] 
		postlist.append(p)
	userg = Userg.objects.get(user=request.user)	
	return render(request, 'allposts.html', { "postlist":postlist , "userg":userg }  )

def edit_post(request,post):
	p = Post.objects.get(id=post.id)
        return render_to_response('edit_post.html', {  "post":p } )

def hello_world(request,word):
	if (word==''):
		word = 'DefaultWorldWord'
	return render_to_response('hellow.html', { "word":word } )

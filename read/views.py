from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.http import Http404
from write import models

# Create your views here.

def read(request):
	if request.user.is_authenticated:
		try:
			data = models.Writing.objects.all()
			latest = models.Writing.objects.latest('id')
		except:
			data = ''
			latest = ''
			
		return render(request, 'read/read.html', 
			{'data': data, 
			'latest': latest, 
			'view_title': 'Recent'})
	else:
		return render(request, 'write/login.html')


		# if request.method == 'POST':
		# 	username = request.POST['username']
		# 	password = request.POST['password']
		# 	user = authenticate(request, username=username, password=password)
		# 	if user is not None:
		# 		login(request, user)
		# 		return render(request, 'read/read.html')
		# 	else:
		# 		return render(request, 'write/login.html', {'error': 'User does not exist!'})
		# return render(request, 'write/login.html')

def readMiniDay(request, id):
	try:
		data = models.Writing.objects.all()
		content = models.Writing.objects.get(id=id)
		return render(request, 'read/read_view.html', 
			{'data': data,
			 'content': content,
			 'view_title': content.date_created
			 })
	except:
		 raise Http404("No matches the given query.")
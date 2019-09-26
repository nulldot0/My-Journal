from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from .models import Writing as Write
from .forms import Writing	

# Create your views here.
def write(request):
	if request.user.is_authenticated:
		form = Writing()
		return render(request, 'write/write.html', {'form': form})

	else:
		return redirect('/login')

def writing(request):
	if request.method == 'POST':
		form = Writing(request.POST)
		if form.is_valid():
			obj = Write()
			obj.content = form.cleaned_data['content']
			obj.save()
		return	redirect('/read')

def login(request):
	if not request.user.is_authenticated:
		return render(request, 'write/login.html')
	else:
		return redirect('/write')

def loging_in(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		the_user = authenticate(request, username=username, password=password)
		if the_user is not None:
			auth_login(request, the_user)
			return redirect('/write')
		else:
			return render(request, 'write/login.html', {'error': 'User does not exist'})
	else:
		return redirect('/write')
			
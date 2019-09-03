from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
import datetime
from .models import Writing as Write
from .forms import Writing	

# Create your views here.
def write(request):
	if request.user.is_authenticated:
		if request.method == 'POST':
			form = Writing(request.POST)
			if form.is_valid():
				obj = Write()
				obj.content = form.cleaned_data['content']
				obj.save()
				form = Writing()
				return render(request, 'main/base.html', {'form': form})

		else:
			form = Writing()
			return render(request, 'write/write.html', {'form': form})
	else:
		if request.method == 'POST':
			username = request.POST['username']
			password = request.POST['password']
			user = authenticate(request, username=username, password=password)
			if user is not None:
				login(request, user)
				form = Writing()
				return render(request, 'write/write.html', {'form': form})
		else:
			return render(request, 'write/login.html')


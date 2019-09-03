from django.shortcuts import render
from django.contrib.auth import authenticate, login
# Create your views here.
def main(request):
	return render(request, 'main/base.html')

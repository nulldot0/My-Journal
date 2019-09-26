from django.shortcuts import render
from apiclient.discovery import build
import json
from django.http import HttpResponse
# Create your views here.
def watch(request):
		return render(request, 'watch/base.html')

def jsons(request):
	try:
		x = request.GET['query']
	except:
		x = False
	if x:
		query = request.GET['query']
		api_key = 'AIzaSyCcgEDU-MitRkYaLc8uH80K7DGibC0N3Ys'
		youtube = build('youtube', 'v3', developerKey=api_key)
		req = youtube.search().list(q=query, part='snippet', type='video')
		res = req.execute()
		items = res['items']
		res = json.dumps(items)
		return HttpResponse(res)
	else:
		return HttpResponse('no_data')
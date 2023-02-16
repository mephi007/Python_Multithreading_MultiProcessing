from django.shortcuts import render

from django.http import HttpResponse
from .tasks import downloadImagesWithThreading2

def index(request):
    downloadImagesWithThreading2.delay()
    return HttpResponse("download")

def test(request):
	return HttpResponse("ok")
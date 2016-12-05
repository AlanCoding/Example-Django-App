# Django
from django.shortcuts import render
from django.http import HttpResponse

# Celery
from celery import Celery

# Python
import time

# Apps
from async import celery

# Views
def slow_page(request):
	"""A page that loads very slowly due to wait."""
	print("starting long wait")
	time.sleep(5)
	print("ended long wait")
	return HttpResponse('Finished waiting for 5 seconds')


def fast_page(request):
	"""A page that loads fast but starts something in the background."""
	print("starting fast-page long wait")
	celery.hello.delay()
	return HttpResponse('Started thread for waiting for 5 seconds')


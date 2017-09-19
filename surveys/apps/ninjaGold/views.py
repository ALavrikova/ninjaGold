# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import random

from django.shortcuts import render,redirect

def index(request):
	return render(request, 'ninjaGold/index.html')

def process_money(request):
	try:
		request.session['money'],
		request.session['total'],
		request.session['log']
	except KeyError:	
		request.session['money'] = 0
		request.session['total'] = 0
		request.session['log'] = []

	if 'farm' in request.POST['building']:
		# building = request.POST['building']
		request.session['money'] = random.randint(10,20)
		request.session['total'] += request.session['money']
		request.session['log'].append("You just earned " + str(request.session['money']) + " gold from the farm")

	elif 'cave' in request.POST['building']:
		# building = request.POST['building']
		request.session['money'] = random.randint(5,10)
		request.session['total'] += request.session['money']
		request.session['log'].append("You just earned " + str(request.session['money']) + " gold from the cave")	

	if 'house' in request.POST['building']:
		# building = request.POST['building']
		request.session['money'] = random.randint(2,5)
		request.session['total'] += request.session['money']
		request.session['log'].append("You just earned " + str(request.session['money']) + " gold from the house")

	if 'casino' in request.POST['building']:
		# building = request.POST['building']
		request.session['money'] = random.randint(0,50)
		request.session['total'] -= request.session['money']
		request.session['log'].append("You just lost " + str(request.session['money']) + " gold to the casino!")

	return redirect('/')	

def round(request):
	return redirect('/')	
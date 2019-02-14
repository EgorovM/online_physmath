# -*- coding: utf-8 -*-

from django.shortcuts 			import render, HttpResponseRedirect, redirect
from .models					import Pupil, Order
from django.db 					import IntegrityError
from django.core.paginator 		import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.models import User
from django.contrib.auth 		import authenticate
from django.contrib.auth 		import logout
from django.contrib 			import auth
from PIL      					import Image
from pytz 						import timezone
from datetime 					import datetime, timedelta

import pytz
import json
import operator
from io import StringIO
import threading

value = {"school_enter":"present","school_exit":"leave"}

secret_word = "axaxloleslivslomaesh"

translate = {
	"absent": "Отсуствует"
}

ykt_utc = timezone('Asia/Yakutsk')

def information(request):
	context = {}

	pupils = Pupil.objects.all()
	pupils_list = sorted(pupils, key = operator.attrgetter('grade','name'))

	context["pupils"] = pupils_list
	context["translate"] = translate
	request = render(request, 'main/information.html', context)

	return request


def index(request):
	context = {}

	if request.GET.get("qrcode") and request.GET.get("secret_word"):
		get_secret_word = request.GET["secret_word"]

		if get_secret_word == secret_word:
			qrcode = request.GET["qrcode"]

			pupil 			  = Pupil.objects.get(qrcode = qrcode)
			date_time = str(datetime.now(tz = ykt_utc).date()) + " " + str(datetime.now(tz = ykt_utc).hour) + ":" + str(datetime.now(tz = ykt_utc).minute)

			if request.GET["location"] == "board_enter":
				if pupil.inboard != True:
					pupil.events.append(date_time + " пришел в интернат")
				pupil.inboard = True

			elif request.GET["location"] == "board_exit":
				if pupil.inboard != False:
					pupil.events.append(date_time + " вышел из интерната")
				pupil.inboard = False

			elif request.GET["location"] == "Canteen":
				if pupil.eating != True:
					pupil.events.append(date_time + " пришел в столовую")
				pupil.eating = True

			else:
				if request.GET["location"] == "school_enter" and pupil.status != "present":
					pupil.events.append(date_time + " пришел в школу")
				elif request.GET["location"] == "school_exit" and pupil.status != "absent":
					pupil.events.append(date_time + " вышел из школы")

				pupil.status 	  = value[request.GET["location"]]
				pupil.arrive_time =  datetime.now(tz = ykt_utc).time()


			pupil.save()


	request = render(request, 'main/index.html', context)

	return request

def monitoring(request):
    context = {}

    pupils = Pupil.objects.all()
    pupils_list = sorted(pupils, key=operator.attrgetter('grade','location','name'))

    context["pupils_list"] = pupils_list

    request = render(request, 'main/monitoring.html', context)

    return request

def about(request):
    context = {}

    if request.method == "POST":
        if "ok_button" in request.POST:
            email   = request.POST["email"]
            school  = request.POST["school"]
            message = request.POST["message"]

            order = Order()

            order.email = email
            order.school_name = school
            order.message = message
            order.date = datetime.now(tz = ykt_utc)

            order.save()

    request = render(request, 'main/about.html')

    return request


def board(request):
    context = {}

    pupils = Pupil.objects.filter(location = "boarding")
    pupils_list = sorted(pupils, key=operator.attrgetter('grade','name'))

    context["pupils"] = pupils_list

    request = render(request, 'main/board.html', context)

    return request

def canteen(request):
    context = {}

    pupils = Pupil.objects.all()
    pupils_list = sorted(pupils, key=operator.attrgetter('grade','name'))

    context["pupils"] = pupils_list

    request = render(request, 'main/canteen.html', context)

    return request

def profile(request, views_profile_id):
	context = {}
	profile = Pupil.objects.get(id = views_profile_id)
	context["profile"] = profile

	request = render(request, "main/profile.html", context)

	return request

def refresh(request):
	pupils = Pupil.objects.all()

	for pupil in pupils:
		if pupil.status == "absent":
			pupil.non_attendance += 1

		pupil.status = "absent"

		pupil.save()

	return redirect('/')
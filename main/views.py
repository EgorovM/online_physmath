# -*- coding: utf-8 -*-

from django.shortcuts 			import render, HttpResponseRedirect, redirect
from .models					import Pupil, Order, Event, Day
from django.db 					import IntegrityError
from django.core.paginator 		import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.models import User
from django.contrib.auth 		import authenticate
from django.contrib.auth 		import logout
from django.contrib 			import auth
from PIL      					import Image
from pytz 						import timezone
from datetime 					import datetime, timedelta
from django.http 				import JsonResponse
import pytz
import json
import operator
from io import StringIO
import threading

value = {"school_enter":"present","school_exit":"leave"}

secret_word = "axaxloleslivslomaesh"

ykt_utc = timezone('Asia/Yakutsk')

def information(request):
	context = {}

	pupils = Pupil.objects.all()
	pupils_list = sorted(pupils, key = operator.attrgetter('grade','name'))

	context["pupils"] = pupils_list
	context["in_school"] = len(Pupil.objects.filter(status = "present"))
	context["pupils_amt"] = len(pupils)

	request = render(request, 'main/information.html', context)

	return request


def index(request):
	context = {}

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

    context["in_board"] = len(Pupil.objects.filter(location = "boarding", inboard = True))
    context["pupils_amt"] = len(pupils)
    context["pupils"] = pupils_list

    request = render(request, 'main/board.html', context)

    return request

def canteen(request):
    context = {}

    pupils = Pupil.objects.all()
    pupils_list = sorted(pupils, key=operator.attrgetter('grade','name'))

    context["pupils"] = pupils_list
    context["eating_amt"] = len(Pupil.objects.filter(eating = True))
    context["pupils_amt"] = len(pupils)

    request = render(request, 'main/canteen.html', context)

    return request

def profile(request, views_profile_id):
	context = {}
	context["is_admin"] = False

	if request.user.is_authenticated():
		context["is_admin"] = True


	profile = Pupil.objects.get(id = views_profile_id)
	events  = Event.objects.filter(profile = profile)

	if request.method == "POST":
		event = Event(profile = profile)

		if "enter" in request.POST:
			profile.status = "present"
			event.text = "пришел в школу"
			event.color = "#8bc34a"
		elif "eating" in request.POST:
			profile.eating = True
			event.text = "пришел в столовую"
			event.color = "#2196f3"
		elif "exit" in request.POST:
			profile.status = "absent"
			event.text = "вышел из школы"
			event.color = "#f44336"

		event.time = datetime.now(tz = ykt_utc).time()
		profile.arrive_time =  datetime.now(tz = ykt_utc).time()

		profile.save()
		event.save()

	context["events"]  = events
	context["profile"] = profile

	request = render(request, "main/profile.html", context)

	return request

def mark(request):
    get_index = "-1"

    if request.GET.get("index") and request.GET.get("secret_word"):
        get_secret_word = request.GET["secret_word"]

        if get_secret_word == secret_word:
            get_index = request.GET["index"]

            pupil      = Pupil.objects.get(index = get_index)
            day        = datetime.now(tz = ykt_utc)
            Attendance = Day.objects.get(date = day)
            time       = day.time()

            if request.GET["location"] != "school_canteen":
                pupil.arrive_time =  time
                event = Event(time = time)

            if request.GET["location"] == "school_enter":
                if pupil.status != "present":
                    if not pupil in Attendance.pupil.get_queryset():
                        print("if1")
                        Attendance.pupil.add(pupil)
                        Attendance.save()

                    event.text = "пришел в школу"
                    event.color = "#8bc34a"
                    pupil.status = "present"
                    print("if2")
                else:
                    event.text = "вышел из школы"
                    event.color = "#f44336"
                    pupil.status = "leave"

            elif request.GET["location"] == "board_enter":
                if pupil.inboard == False:
                    event.text = "пришел в интернат"
                    event.color =  event.color = "#cddc39"
                    pupil.inboard = True
                else:
                    event.text = "вышел из интерната"
                    event.color = "#ff9800"
                    pupil.inboard = False

            elif request.GET["location"] == "school_canteen":
                event.text = "пришел в столовую"
                event.color = "#2196f3"
                pupil.eating = True

            if event.text != "":
                event.profile = pupil
                event.save()

            pupil.save()

    elif request.GET.get("qrcode") and request.GET.get("secret_word"):
        get_secret_word = request.GET["secret_word"]

        if get_secret_word == secret_word:

            qrcode = request.GET["qrcode"]

            pupil 			  = Pupil.objects.get(qrcode = qrcode)
            day        = datetime.now(tz = ykt_utc)
            Attendance = Day.objects.get(date = day)
            time       = day.time()
            event = Event(time = time)

            if request.GET["location"] == "board_enter":
                if pupil.inboard != True:
                    event.text =  "пришел в интернат"
                    event.color = "#cddc39"

                pupil.inboard = True

            elif request.GET["location"] == "board_exit":
                if pupil.inboard != False:
                    event.text  =  "вышел из интерната"
                    event.color = "#ff9800"

                pupil.inboard = False

            elif request.GET["location"] == "Canteen":
                if pupil.eating != True:
                    event.text  = "пришел в столовую"
                    event.color = "#2196f3"

                pupil.eating = True

            else:
                if request.GET["location"] == "school_enter" and pupil.status != "present":
                    if not pupil in Attendance.pupil.get_queryset():
                        Attendance.pupil.add(pupil)
                        Attendance.save()
                    event.text  = "пришел в школу"
                    event.color = "#8bc34a"

                elif request.GET["location"] == "school_exit" and pupil.status == "present":
                    event.text =  "вышел из школы"
                    event.color = "#f44336"

                pupil.status 	  = value[request.GET["location"]]
                pupil.arrive_time =  datetime.now(tz = ykt_utc).time()

                if event.text != "":
                    event.profile = pupil
                    event.save()

                pupil.save()

    elif request.GET.get("get_profile") and request.GET.get("secret_word"):
        get_secret_word = request.GET["secret_word"]
        get_index =  request.GET["get_profile"]

        if get_secret_word == secret_word:
            if not Pupil.objects.filter(index=get_index).exists():
            	return JsonResponse({"profile": [{"index": "-1"}]})
            else:
            	profile = Pupil.objects.values('index', 'name', 'grade', 'photo').filter(index = get_index)

            return JsonResponse({'profile': list(profile)})

    return HttpResponseRedirect("/")



def refresh(request):
	if request.user.is_authenticated():
		pupils = Pupil.objects.all()
		Event.objects.all().delete()

		for pupil in pupils:
			if pupil.status == "absent":
				pupil.non_attendance += 1

			pupil.status = "absent"

			pupil.save()

	return HttpResponseRedirect('/')

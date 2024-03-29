# -*- coding: utf-8 -*-

from django.shortcuts 			import render, HttpResponseRedirect, redirect, HttpResponse
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
from io import StringIO
import pandas as pd
import mimetypes
import threading
import operator
import sqlite3
import json
import pytz
import os


value = {"school_enter":"present","school_exit":"leave"}

secret_word = "axaxloleslivslomaesh"

ykt_utc = timezone('Asia/Yakutsk')


def information(request):
    if not request.user.is_authenticated():
        return redirect("/")

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

    if request.user.is_authenticated():
        context["is_auth"] = True

    request = render(request, 'main/index.html', context)

    return request

def monitoring(request):
    if not request.user.is_authenticated():
        return redirect("/")
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
    if not request.user.is_authenticated():
        return redirect("/")
    context = {}

    pupils = Pupil.objects.filter(location = "boarding")
    pupils_list = sorted(pupils, key=operator.attrgetter('grade','name'))

    context["in_board"] = len(Pupil.objects.filter(location = "boarding", inboard = True))
    context["pupils_amt"] = len(pupils)
    context["pupils"] = pupils_list

    request = render(request, 'main/board.html', context)

    return request

def canteen(request):
    if not request.user.is_authenticated():
        return redirect("/")
    context = {}

    pupils = Pupil.objects.all()
    pupils_list = sorted(pupils, key=operator.attrgetter('grade','name'))

    context["pupils"] = pupils_list
    context["eating_amt"] = len(Pupil.objects.filter(eating = True))
    context["pupils_amt"] = len(pupils)

    request = render(request, 'main/canteen.html', context)

    return request

def profile(request, views_profile_id):
    if not request.user.is_authenticated():
        return redirect("/")
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
    	elif "exit_board" in request.POST:
    		profile.inboard = False
    		event.text = "вышел из интерната"
    		event.color = "#ff9800"
    	elif "enter_board" in request.POST:
    		profile.inboard = True
    		event.text = "пришел в интернат"
    		event.color = "#cddc39"
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
    elif request.GET.get("get_products"):
        return JsonResponse({"products": [{"name": "A4", "category": "paper"}]})

    return HttpResponseRedirect("/")



def get_attendance_list(request):
    excel_file_name = "Посещаемость в школе.xlsx"

    d = {}

    conn = sqlite3.connect('/home/EgorovM/online_physmath/db.sqlite3')
    cursor = conn.cursor()

    d = {}

    days       = cursor.execute('SELECT date FROM main_day')
    days_list  = [row[0] for row in days]
    pupil      = cursor.execute('SELECT name FROM main_pupil')
    pupil_list = [row[0] for row in pupil]

    attendance_table = cursor.execute("""
        SELECT
            main_day.date,
        	main_pupil.name
        FROM main_pupil
        	LEFT OUTER join main_day_pupil
            	on main_pupil.id = main_day_pupil.pupil_id
            LEFT OUTER JOIN main_day
            	on main_day.id = main_day_pupil.day_id
    """)

    for name in pupil_list:
        d[name] = [0 for i in range(len(days_list))]

    for row in attendance_table:
        try:
            d[row[1]][days_list.index(row[0])] = 1
        except:
            pass


    data = pd.DataFrame.from_dict(data = d, orient='index',
                        columns = days_list)
    writer = pd.ExcelWriter(excel_file_name, engine='xlsxwriter')
    data.to_excel(writer, sheet_name = "Attendance")

    workbook  = writer.book
    worksheet = writer.sheets['Attendance']

    cell_format = workbook.add_format({"pattern": 1, "bg_color": "#FDD83C", "align": "left"})

    worksheet.freeze_panes(1,1)
    worksheet.set_column('A:A', 30, cell_format)
    worksheet.set_column('B:AIT', 15)

    writer.save()

    fp = open(excel_file_name, "rb");
    response = HttpResponse(fp.read());
    fp.close();

    file_type = mimetypes.guess_type(excel_file_name);

    if file_type is None:
        file_type = 'application/octet-stream';

    response['Content-Type'] = file_type
    response['Content-Length'] = str(os.stat(excel_file_name).st_size);
    response['Content-Disposition'] = "attachment; filename=Attendance.xlsx";

    return response;

def refresh(request):
    if request.user.is_authenticated() or (request.GET.get("secret_word") and request.GET["secret_word"] == secret_word):
        day = Day.objects.create(date = (datetime.now(tz = ykt_utc)))

        pupils = Pupil.objects.all()
        Event.objects.all().delete()

        for pupil in pupils:
            if pupil.status == "absent":
                pupil.non_attendance += 1

            pupil.status = "absent"

            pupil.save()

    return HttpResponseRedirect('/')


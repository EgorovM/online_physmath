from django.shortcuts 			import render, HttpResponseRedirect, redirect
from .models					import Pupil
from django.utils 				import timezone
from django.db 					import IntegrityError
from django.core.paginator 		import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.models import User
from django.contrib.auth 		import authenticate
from django.contrib.auth 		import logout
from django.contrib 			import auth
from django.utils 				import timezone
from PIL      					import Image
import datetime
import pytz
import json
import operator
from io import StringIO
import threading

secret_word = "axaxloleslivslomaesh"

translate = {
	"absent": "Отсуствует"
}

def information(request):
	context = {}



	pupils = Pupil.objects.all()
	pupils_list = sorted(pupils, key = operator.attrgetter('name'))

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
            pupil.status 	  = "present"
            pupil.arrive_time =  timezone.localtime(timezone.now())

            pupil.save()

    request = render(request, 'main/index.html', context)

    return request

def monitoring(request):
	context = {}

	pupils = Pupil.objects.all()
	pupils_list = sorted(pupils, key=operator.attrgetter('location','name'))

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
            order.date = timezone.now()

            order.save()

    request = render(request, 'main/about.html')

    return request

def refresh(request):
	pupils = Pupil.objects.all()

	for pupil in pupils:
		if pupil.status == "absent":
			pupil.non_attendance += 1

		pupil.status = "absent"

		pupil.save()

	return redirect('/')
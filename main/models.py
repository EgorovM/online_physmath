# -*- coding: utf-8 -*-

from __future__                     import unicode_literals
from django.utils.encoding          import python_2_unicode_compatible
from django.db                      import models
from django.contrib.auth.models     import User
from datetime 					    import datetime
from django 						import forms

LOCATION = (
    ("urban", "Городской"),
    ("boarding", "Интернат"),
    ("relativity", "У родственников")
)

STATUS = (
	("absent",  "Отсутствует"),
	("present", "Присутствует"),
	("ill",     "Болеет"),
	("reason",  "Уважительная причина"),
)

GRADE = (
	("11FM","11 физико-математический класс"),
	("11ENG","11 инженерный класс"),
	("11TECH","11 технический класс"),
	("11PTH","11 политехнический класс"),
	("11BCH","11 биолого-химический класс"),
	("11HUM","11 гуманитарный класс"),
	("10FM","10 физико-математический"),
	("10ENG","10 инженерный класс"),
	("10TECH","10 технический класс"),
	("10PTH","10 политехнический класс"),
	("10BCH","10 биолого-химический класс"),
	("10HUM","10 гуманитарный класс"),
	("9","9"),
	("8","8"),
	("7","7"),
	("6","6"),
	("5","5"),
)

class Pupil(models.Model):
	qrcode      = models.CharField(max_length = 50)
	name        = models.CharField(max_length = 50)
	grade       = models.CharField(max_length = 50, choices = GRADE)
	location    = models.CharField(max_length = 50, choices = LOCATION) 
	status      = models.CharField(max_length = 50, default = "absent", choices = STATUS)

	arrive_time	   = models.TimeField('time arrive', null = True, blank = True)
	photo     	   = models.ImageField(upload_to = "images/", default = "images/default.jpg")
	non_attendance = models.IntegerField(default = 0);

	def __str__(self):
		return str(self.qrcode)

class Order(models.Model):
	email       = models.CharField(max_length = 70)
	school_name = models.CharField(max_length = 100)
	message     = models.CharField(max_length = 300)
	date        = models.DateTimeField('order date',)

	def __str__(self):
		return str(self.school_name)
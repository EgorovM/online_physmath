from __future__                     import unicode_literals
from django.utils.encoding          import python_2_unicode_compatible
from django.db                      import models
from django.contrib.auth.models     import User
from django.utils 					import timezone
from django 						import forms

class Pupil(models.Model):
	qrcode      = models.CharField(max_length = 50)
	name        = models.CharField(max_length = 50)
	grade       = models.CharField(max_length = 50)
	location    = models.CharField(max_length = 50) 
	status      = models.CharField(max_length = 50, default = "absent")

	arrive_time = models.DateTimeField('date arrive')
	photo     = models.ImageField(upload_to = "images/", default = "images/default.jpg")
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
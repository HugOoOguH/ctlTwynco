from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


class Mark(models.Model):
	name = models.CharField(max_length=50)
	description = models.TextField()
	image = models.ImageField(upload_to='imageMarks',max_length=100, height_field=None, width_field=None,blank=True)
	visits = models.IntegerField(blank=True, null=True)
	slug = models.SlugField(max_length=140)

	class Meta:
		verbose_name = "Mark"
		verbose_name_plural = "Marks"

	def __str__(self):
		return self.name


class Coupon(models.Model):
	mark_coupon = models.ForeignKey(Mark, related_name='coupons_mark')
	prize = models.CharField(max_length=100)
	description = models.TextField()
	start_date = models.DateField()
	final_date = models.DateField()
	coins = models.IntegerField(blank=True, null=True)

	class Meta:
		verbose_name = "Coupon"
		verbose_name_plural = "Coupons"

	def __str__(self):
		return self.prize

class Exchanged_Coupon(models.Model):
	coupon_exhanged = models.ForeignKey('Coupon', related_name='exchanged_cupon',)
	user_coupon = models.ForeignKey(User, related_name='coupons_user',)
	status = models.BooleanField(default=False)
	exchanged_date = models.DateField(auto_now=True)

	class Meta:
		verbose_name = "Exchanged_Coupon"
		verbose_name_plural = "Exchanged_Coupons"

            
# Create your models here.

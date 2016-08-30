from __future__ import unicode_literals
from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

# Create your models here.
class Profile(models.Model):
	user = models.OneToOneField(settings.AUTH_USER_MODEL)
	coins = models.IntegerField(blank=True, null=True)
	photo = models.ImageField(upload_to="users/%Y/%m/%d", blank=True)

	class Meta:
		ordering = ('user',)

	def __str__(self):
		return 'Perfil del usuario {}'.format(self.user.username)
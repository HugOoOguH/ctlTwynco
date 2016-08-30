from django.contrib import admin
from .models import Profile
# Register your models here.
class ProfileAdmin(admin.ModelAdmin):
	list_display = (
		'user',
		'coins',
		'photo',
		)

	list_filter = ('user',)
	search_fields = ('user','coins')
	ordering = ['user']

admin.site.register(Profile, ProfileAdmin)
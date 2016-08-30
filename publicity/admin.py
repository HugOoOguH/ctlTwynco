from django.contrib import admin
from .models import Mark, Coupon, Exchanged_Coupon
# Register your models here.
# 
class MarkAdmin(admin.ModelAdmin):
    '''
    Admin View for Mark
    '''
    list_display = ('name','visits',)
    list_filter = ('visits', 'name',)
    search_fields = ('name','slug',)
    prepopulated_fields = {'slug':('name',)}
    ordering = ['name']		

class CouponAdmin(admin.ModelAdmin):
    '''
        Admin View for Coupon
    '''
    list_display = ('prize',
    	'start_date', 
    	'final_date', 
    	'coins',)
    
    list_filter = ('prize',)
    search_fields = ('prize','coins',)
    ordering = ['final_date']


class Exchanged_CouponAdmin(admin.ModelAdmin):
    '''
        Admin View for Exchanged_Coupon
    '''
    list_display = ('user_coupon','status','exchanged_date',)
    list_filter = ('status',)
    search_fields = ('exchanged_date',)
    raw_id_fields = ("user_coupon",)
    ordering = ['exchanged_date']

admin.site.register(Mark,MarkAdmin)
admin.site.register(Coupon,CouponAdmin)
admin.site.register(Exchanged_Coupon,Exchanged_CouponAdmin)


from django.contrib import admin

from .models import Flat, Complaint

 
class FlatAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at',)
    search_fields = ('town','address','owner',)
    list_display = ('address', 'price', 'new_building', 'construction_year', 'town', 'owner_phone_pure')
    list_editable = ('new_building',)
    list_filter = ('new_building',)
    raw_id_fields = ('likes',)
 

class ComplaintAdmin(admin.ModelAdmin):
    raw_id_fields = ('flat',)

admin.site.register(Flat, FlatAdmin) 
admin.site.register(Complaint, ComplaintAdmin)
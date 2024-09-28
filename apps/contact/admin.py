from django.contrib import admin
from . models import Contact

# Register your models here.
class ContactAdmin(admin.ModelAdmin):
	list_display = ('id', 'created_at', 'name', 'mobile', 'email', 'address', 'service', 'deadline', 'budget', 'message')

admin.site.register(Contact, ContactAdmin) 
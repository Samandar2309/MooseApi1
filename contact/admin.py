from django.contrib import admin
from .models import ContactInfo, Contact, Subscribe


# Register your models here.

class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'email')
    list_filter = ('name', 'email')


admin.site.register(Contact, ContactAdmin)
admin.site.register(Subscribe)
admin.site.register(ContactInfo)

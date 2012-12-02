from django.contrib import  admin
from pay.models import Person,Record

class PersonAdmin(admin.ModelAdmin):
	# display_line = []
	pass

class RecordAdmin(admin.ModelAdmin):
	pass

admin.site.register(Person,PersonAdmin)
admin.site.register(Record,RecordAdmin)
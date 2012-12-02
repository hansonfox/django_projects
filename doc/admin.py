from django.contrib import admin
from doc.models import Doc#,Record 

class DocAdmin(admin.ModelAdmin):
    pass

# class RecordAdmin(admin.ModelAdmin):
#     pass	

admin.site.register(Doc,DocAdmin)
# admin.site.register(Record,RecordAdmin)

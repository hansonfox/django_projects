from django.contrib import admin
from rent.models import Contract,Pr

class ContractAdmin(admin.ModelAdmin):
	pass
class PrAdmin(admin.ModelAdmin):
	pass

admin.site.register(Contract,ContractAdmin)
admin.site.register(Pr,PrAdmin)

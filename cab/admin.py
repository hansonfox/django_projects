from django.contrib import admin
from cab.models import Language,Snippet

class LanguageAdmin(admin.ModelAdmin):
	pass

class SnippetAdmin(admin.ModelAdmin):
	pass


admin.site.register(Language,LanguageAdmin)
admin.site.register(Snippet,SnippetAdmin)
# admin.site.register(Link,LinkAdmin)

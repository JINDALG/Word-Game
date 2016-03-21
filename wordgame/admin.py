from django.contrib import admin
from .models import Quiz,User

class QuizAdmin(admin.ModelAdmin):
	list_display = ['id','word','meaning','phrase','sentence','image_url']

	list_editable = ['id','meaning','phrase','sentence','image_url']
admin.site.register(Quiz,QuizAdmin)
admin.site.register(User)




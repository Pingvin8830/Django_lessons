from django.contrib import admin
from .models        import Question, Choice

# Register your models here.
# admin.site.register (Question)

class QuestionAdmin (admin.ModelAdmin):
	fieldsets = [
		(None,               {'fields': ['question_text']}),
		('Date information', {'fields': ['pub_date']}),
	]

class QuestionAdmin_old (admin.ModelAdmin):
	fields = [
		'pub_date',
		'question_text'
	]

admin.site.register (Question, QuestionAdmin)
admin.site.register (Choice)

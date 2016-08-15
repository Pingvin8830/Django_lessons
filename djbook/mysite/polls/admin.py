from django.contrib import admin
from .models        import Question, Choice

# Register your models here.
# admin.site.register (Question)
# admin.site.register (Choice)

class ChoiceInline (admin.TabularInline):
# class ChoiceInline (admin.StackedInline):
	model = Choice
	extra = 3

class QuestionAdmin (admin.ModelAdmin):
	fieldsets = [
		(None,               {'fields': ['question_text']}),
		('Date information', {'fields': ['pub_date']}),
	]
	inlines = [ChoiceInline]

class QuestionAdmin_old (admin.ModelAdmin):
	fields = [
		'pub_date',
		'question_text'
	]

admin.site.register (Question, QuestionAdmin)

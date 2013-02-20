from polls.models import Poll
from polls.models import Choice
from django.contrib import admin

class ChoiceInline(admin.TabularInline):
	model = Choice
	extra = 3

class PollAdmin(admin.ModelAdmin):
	list_display=('question', 'pub_date', 'was_published_today') #ordering & tuple of field name to display on the change list page of the object
	list_filter = ['pub_date'] #adds a filter sidebar that lets user filter the change list by pub_date
	search_fields = ['question'] #search box at the top of the change list, searches the question field
	date_hierachy = 'pub_date' #drill down by date, hierachical navigation

	fieldsets = [
		(None, 				{'fields': ['question']}),
		('Date information',{'fields': ['pub_date'], 'classes': ['collapse']}),
	]
	inlines = [ChoiceInline]

admin.site.register(Poll, PollAdmin)

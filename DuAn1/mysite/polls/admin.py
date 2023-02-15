from django.contrib import admin
from .models import Choice, Question
# Register your models here.
class QuestionAdmin(admin.ModelAdmin):
    list_display= ['question_text','time_pub' ]
    search_fields= ['time_pub']
class ChoiceAdmin(admin.ModelAdmin):
    list_display= ['question','choice_text', 'vote' ]
    search_fields= ['choice_text']
    list_filter=['question', "choice_text", 'vote']
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice, ChoiceAdmin)
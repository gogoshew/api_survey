from django.contrib import admin
from .models import Survey, Question, Answer, Choice


@admin.register(Survey, Question, Answer, Choice)
class SurveyAdmin(admin.ModelAdmin):
    pass
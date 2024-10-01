from django.contrib import admin
from unfold.admin import ModelAdmin

from .models import Question


# Register your models here.
@admin.register(Question)
class QuestionAdmin(ModelAdmin):
  pass

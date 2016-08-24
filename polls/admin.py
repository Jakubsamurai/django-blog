from django.contrib import admin
from .models import Question


class AuthorAdmin(admin.ModelAdmin):
    pass


admin.site.register(Question, AuthorAdmin)

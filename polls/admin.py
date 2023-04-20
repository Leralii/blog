from django.contrib import admin

from .models import Question

admin.site.register(Question)
# TODO add choice

from .models import Choice

admin.site.register(Choice)


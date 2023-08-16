from django.contrib import admin
from .models import Task, Company, User, Feedback

admin.site.register(Task)
admin.site.register(Company)
admin.site.register(User)
admin.site.register(Feedback)

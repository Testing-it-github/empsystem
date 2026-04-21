from django.contrib import admin
from .models import Employee,Latestnews,Calendar,JobOpening

# Register your models here.
admin.site.register(Employee)
admin.site.register(Latestnews)
admin.site.register(Calendar)
admin.site.register(JobOpening)

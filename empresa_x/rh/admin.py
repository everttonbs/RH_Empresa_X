from django.contrib import admin
from .models import *

# Register your models here.

class EmployerAdmin(admin.ModelAdmin):
    fields = ()
    list_display = (('first_name'), ('last_name'), ('email'))
    list_filter = ()
    search_fields = (('first_name'), )


admin.site.register(Employer, EmployerAdmin)




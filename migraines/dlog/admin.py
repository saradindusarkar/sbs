from django.contrib import admin

# Register your models here.
from dlog.models import Dlog



class DlogAdmin(admin.ModelAdmin):
    """ list_display = [ 'log_date'] """

admin.site.register(Dlog, DlogAdmin)


from django.contrib import admin


from dlog.models import user_login,migraines_log

# Register your models here.
#

admin.site.register(user_login)
admin.site.register(migraines_log)
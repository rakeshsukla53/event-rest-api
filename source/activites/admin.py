from django.contrib import admin
from .models import Activity
# Register your models here.
class ActivityAdmin(admin.ModelAdmin):
    pass

admin.site.register(Activity)

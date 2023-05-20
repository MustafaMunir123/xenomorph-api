from django.contrib import admin
from xenomorph_api.apps.tracking.models import Tracks, Mark

# Register your models here.

admin.site.register(Tracks)
admin.site.register(Mark)

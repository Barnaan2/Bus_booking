from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Route)
admin.site.register(Single_Bus)
admin.site.register(SubRoute)
admin.site.register(Seat)

admin.site.register(SubRouteAdmin)
admin.site.register(SubRouteBusAdmin)

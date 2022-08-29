from django.contrib import admin
from .models import Route ,Bus,SubRouteAdmin
# Register your models here.
  
admin.site.register(Route) 
admin.site.register(Bus)
admin.site.register(SubRouteAdmin)
# admin.site.register(SubRoute)
# admin.site.register(Seat)

# admin.site.register(SubRouteAdmin)
# admin.site.register(SubRouteBusAdmin)

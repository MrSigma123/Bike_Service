from django.contrib import admin
from .models import *

admin.site.register(User)
admin.site.register(RepairRequest)
admin.site.register(ServiceOrder)
admin.site.register(Diagnosis)
admin.site.register(RepairReport)
admin.site.register(Part)
admin.site.register(UsedPart)
admin.site.register(Notification)
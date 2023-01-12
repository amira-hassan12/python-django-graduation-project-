from django.contrib import admin

# Register your models here.


from .models import *

admin.site.register(Patient)

admin.site.register(Doctor)

admin.site.register(Ask)
admin.site.register(Answer)
admin.site.register(Center)
admin.site.register(Review)

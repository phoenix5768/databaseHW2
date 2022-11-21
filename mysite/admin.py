from django.contrib import admin
from .models import Doctor, Publicservant, Record, Specialize, Users, Country, Discover, Disease, Diseasetype

# Register your models here.

admin.site.register(Country)
admin.site.register(Doctor)
admin.site.register(Publicservant)
admin.site.register(Record)
admin.site.register(Specialize)
admin.site.register(Users)
admin.site.register(Discover)
admin.site.register(Disease)
admin.site.register(Diseasetype)
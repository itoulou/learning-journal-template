from django.contrib import admin
from create_resource.models import Resource, Language, Framework, Database, Technology

# Register your models here.
admin.site.register(Resource)
admin.site.register(Language)
admin.site.register(Framework)
admin.site.register(Database)
admin.site.register(Technology)
from django.contrib import admin

# Register your models here.
from my_project1.models import Contact
from my_project1.models import Complain

admin.site.register(Contact)
admin.site.register(Complain)
from django.contrib import admin
from mail.models import Email
from django.contrib.auth.models import User

# Register your models here.

admin.site.register(Email)
admin.site.register(User)

from django.contrib import admin

# Register your models here.
from .models import UploadFile, User

# Register your models here.
admin.site.register(User)
admin.site.register(UploadFile)

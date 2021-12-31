from django.contrib import admin
from .models import UploadFile,DownloadFile
admin.site.register(UploadFile)
admin.site.register(DownloadFile)

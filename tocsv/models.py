from django.db import models

class UploadFile(models.Model):
    uploaded_file = models.FileField(upload_to="uploaded/")
    def __str__(self):
        return self.uploaded_file.name
    
class DownloadFile(models.Model):
    new_file_name = models.TextField(blank=True, max_length=50000)
    def __str__(self):
        return self.new_file_name   
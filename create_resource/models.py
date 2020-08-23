import os
from django.db import models

# Create your models here.
class Language(models.Model):
    language = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.language


class Framework(models.Model):
    framework = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.framework


class Database(models.Model):
    database = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.database


class Technology(models.Model):
    technology = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.technology

class Resource(models.Model):
    name = models.CharField(max_length=400)
    link = models.CharField(max_length=1000, blank=True, null=True)
    attachment = models.FileField(upload_to='documents/', blank=True, null=True)
    language = models.ForeignKey(Language, default=None, blank=True, null=True, on_delete=models.CASCADE)
    framework = models.ForeignKey(Framework, default=None, blank=True, null=True, on_delete=models.CASCADE)
    database = models.ForeignKey(Database, default=None, blank=True, null=True, on_delete=models.CASCADE)
    technology = models.ForeignKey(Technology, default=None, blank=True, null=True, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name


    def filename(self):
        return os.path.basename(self.attachment.name)
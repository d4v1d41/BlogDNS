from __future__ import unicode_literals
from django.utils import timezone
from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = RichTextUploadingField()
    image_for_preview = models.ImageField(upload_to='img')
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(default=timezone.now,blank=True, null=True)
    categoria = models.CharField(max_length=256, choices=[('Tramites', 'Tramites'), ('Info', 'Info'), ('Exp', 'Exp')], null=True)
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
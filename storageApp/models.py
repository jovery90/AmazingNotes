from django.db import models
from django.core.urlresolvers import reverse
from django.conf import settings
from django.contrib import auth

from django.contrib.auth import get_user_model
User = get_user_model()

# Create your models here.


class Note(models.Model):
    user = models.ForeignKey(User,related_name='notes')
    title = models.TextField(max_length=20,unique=True)
    created_at = models.DateTimeField(auto_now=True)
    message = models.TextField(max_length=255)
    message_html = models.TextField(editable=False)

    def __str__(self):
        return self.title

    def save(self,*args,**kwargs):
        self.message_html = self.message
        super().save(*args,**kwargs)

    def get_absolute_url(self):
        return reverse('notes:single',kwargs={'username':self.user.username,'pk':self.pk})

    class Meta:
        ordering = ['-created_at']
        unique_together = ['user','title']

class User(auth.models.User,auth.models.PermissionsMixin):

    def __str__(self):
        return self.username
        #username comes from the built in, inherited model

from django.db import models
from django.contrib import auth
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your models here.


class Note(models.Model):
    user = models.ForeignKey(User)
    category = models.CharField(max_length=20)
    title = models.CharField(max_length=20,unique=True)
    note_field = models.TextField(blank=True,default='')

    def __str__(self):
        return self.title

class User(auth.models.User,auth.models.PermissionsMixin):

    def __str__(self):
        return self.username
        #username comes from the built in, inherited model

    notes = models.ForeignKey(Note, related_name='my_notes')

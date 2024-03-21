from django.db import models

# Create your models here.

class EventOrganiser(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

class EventCategory(models.Model):
    cat_name = models.CharField(max_length=100, unique=True)

class event_table(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(default=None)
    date = models.DateField(default=None)
    location = models.CharField(max_length=100, default=None)
    organiser = models.ForeignKey(EventOrganiser, on_delete=models.CASCADE, related_name='organiser', default="Priyank")
    category = models.ForeignKey(EventCategory, on_delete=models.CASCADE, related_name='category', default="Party")
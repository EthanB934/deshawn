"""Appointment database model module"""
from django.db import models

class Appointments(models.Model):
    """Database model for tracking walker appointments"""
    # Datatypes for table values
    completed = models.BooleanField(default=False) 
    # Default value for field is an argument. In this case, 0.
    date = models.DateField()
    # BooleanField, DateField, ForeignKey are classes 
    walker = models.ForeignKey("Walker", on_delete=models.CASCADE, related_name="appointments")
    # There is no need to put "_id" for the foreign key. Instead, we just need the table name

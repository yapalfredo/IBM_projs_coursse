from django.db import models



# Define your first model from here:
class User(models.Model):
    #Charfield for user's first name
    first_name = models.CharField(null=False, max_length=30, default='john')
    #Charfield for user's last name
    last_name = models.CharField(null=False, max_length=30, default='doe')
    #Charfield for user's date of birth
    dob = models.DateField(null=True)
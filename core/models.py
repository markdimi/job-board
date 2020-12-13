from django.db import models


# The database should have one table called `searches` which stores a record of each job search. 
# The `searches` table columns should include time, description, location and ip address of the user.

class Searches(models.Model):
    location = models.CharField(max_length=100, blank=True)
    description = models.CharField(max_length=100, blank=True)
    time = models.DateTimeField(auto_now_add=True)
    ip_address = models.CharField(max_length=100)

from django.db import models

# Create your models here.

class Topic(models.Model):
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)   #Like "GetDate" function in SQL


    def __str__(self):  #This way, when we call the class, it returns back the name and info we put in
        return self.text
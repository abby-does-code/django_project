from django.db import models

# Create your models here.


class Topic(models.Model):
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(
        auto_now_add=True
    )  # Like "GetDate" function in SQL

    def __str__(self):
        return self.text


# Staging changes > committing changes

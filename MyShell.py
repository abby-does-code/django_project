# START

# Use Python skilss to access objects in database to view and test
# Building webpages: code to access and display data
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "learning_log.settings")

import django

django.setup()

from MainApp.models import Topic, Entry

topics = Topic.objects.all()
# query set = list of objects and we can iterate through it

t = Topic.objects.get(id=1)
print(t)

# t.id is automatically assigned
# The Output will actually be names and stuff instead of gibberish bc of __str__ in MainApp.models

entries = t.entry_set.all() #.all gives all the entries; foreign key relationship 


for entry in entries:
    print(entry)

"""
for e in entries:
    print(f"Entry Topic: {e.topic}")
    print(f"Entry Test: {e}")
    print(f" Date Added: {e.date_added}")"""

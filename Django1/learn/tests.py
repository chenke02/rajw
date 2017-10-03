from django.test import TestCase

# Create your tests here.

from learn.models import train_course

k = train_course.objects.filter(Week='1')
print k



from django.db import models


class train_course(models.Model):
    Course = models.CharField(max_length=20)
    People = models.CharField(max_length=20)
    Teacher = models.CharField(max_length=20)
    Section = models.CharField(max_length=20)
    Place = models.CharField(max_length=20)
    Classes = models.CharField(max_length=20)
    Week = models.CharField(max_length=20)


class train_basic(models.Model):
    uid = models.CharField(max_length=20)
    Pastern = models.CharField(max_length=20)
    Build = models.CharField(max_length=20)
    Name = models.CharField(max_length=20)
    Content = models.CharField(max_length=20)
    Power = models.CharField(max_length=20)
    Area = models.CharField(max_length=20)



class train(models.Model):
    Course = models.CharField(max_length=20)

    def __unicode__(self):
        return self.Course
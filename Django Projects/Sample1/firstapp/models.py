from django.db import models
import datetime
from django.utils import timezone

class AllCourses(models.Model):
    coursename=models.CharField(max_length=100)
    insname=models.CharField(max_length=100)
    startedfrom=models.DateTimeField('Started from')

    def __str__(self):
        return self.coursename

    def was_published_recently(self):
        return self.startedfrom >=timezone.now()-datetime.timedelta(days=1)

class Details(models.Model):
    course=models.ForeignKey(AllCourses,on_delete=models.CASCADE)
    ct=models.CharField(max_length=500)
    your_choice=models.BooleanField(default=False)
    #sp=models.CharField(max_length=500)
    #il=models.CharField(max_length=500)

    def __str__(self):
        return str(self.ct)


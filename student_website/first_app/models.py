from django.db import models
from django import forms
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
# Create your models here.
# store your data models where we specify the relationship b/w data

"""
Models created by Samyak Gaur 

The following classes have the following fields

Topics:
->Topic [Primary Key]
    Data:
    - Web Development
    - Machine Learning
    - DSA
    - IoT

Entries:
-->Topic [Foreign Keys]
-->Title
-->Description 
-->Link 
--> PPT 
--> Research Paper [Y/N]
--> Year 
--> Department
-->Grade


"""

YEARS = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
    )
DEPARTMENTS = (
    ('Computers', 'Computers'),
    ('IT', 'IT'),
    ('Electronics', 'Electronics'),
    ('Production', 'Production'),
    ('Mechanical', 'Mechanical'),
)
PAPER =(
    ('YES','YES'),
    ('NO','NO'),
)
class Topic(models.Model):
    topic = models.CharField(max_length=264 , unique=True)

    def __str__(self):
        return self.topic
class Name(models.Model):
    name = models.CharField(max_length=200,default="None")
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey("content_type", "object_id")

    def __str__(self):
        return self.name        

class Entries(models.Model):
    topics = models.ForeignKey(Topic,on_delete=models.PROTECT)
    title = models.CharField(max_length=264, unique=True)
    # name = models.CharField(max_length=264,unique=True)
    description = models.TextField(max_length=600, null=True, blank=True)
    url = models.URLField(unique=True)
    start_date = models.DateField()
    end_date = models.DateField()
    year = models.IntegerField(choices=YEARS, default=1)
    department = models.CharField(max_length=100,choices=DEPARTMENTS,default="Computer")
    research_paper = models.CharField(max_length=100,choices=PAPER,default="NO")
    credits = models.IntegerField(null=True, default=0)
    file= models.FileField(upload_to=None,max_length=100,default="NULL")

    def __str__(self):
        return self.title


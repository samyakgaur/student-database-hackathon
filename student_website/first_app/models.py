from django.db import models
from django import forms
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import User
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
class TeamName(models.Model):
    name = models.CharField(max_length=200,default="None")
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey("content_type", "object_id")

    def __str__(self):
        return self.name

class Notice(models.Model):
    notice_title = models.CharField(max_length=200)
    teacher_name = models.CharField(max_length=300)
    notice = models.TextField(max_length=1000)

    def __str__(self):
        return self.notice_title        

class Mark(models.Model):
    category = models.CharField(max_length=200,default="Mark Category")
    marks = models.IntegerField(null=True, default=0)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey("content_type", "object_id")
    comments=models.CharField(max_length=200, default="none")

    def __str__(self):
        return self.category 


class Entrie(models.Model):
    topics = models.ForeignKey(Topic,on_delete=models.PROTECT)
    name = models.CharField(max_length=100,default="Team leader name Here")
    title = models.CharField(max_length=264, unique=True)
    description = models.TextField(max_length=600, null=True, blank=True)
    url = models.URLField(unique=True)
    start_date = models.DateField()
    end_date = models.DateField()
    year = models.IntegerField(choices=YEARS, default=1)
    department = models.CharField(max_length=100,choices=DEPARTMENTS,default="Computer")
    research_paper = models.CharField(max_length=100,choices=PAPER,default="NO")
    
    
    def __str__(self):
        return self.title
        

class File(models.Model):
    filetype = models.CharField(max_length=200,default="File Type")
    file = models.FileField(blank=True,null=True, default="Null")
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey("content_type", "object_id")

    def __str__(self):
        return self.filetype

class Review(models.Model):
    comment = models.TextField(max_length=500, default="None", null=True)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey("content_type", "object_id")

    def __str__(self):
        return self.comment 
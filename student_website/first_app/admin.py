from django.contrib import admin
from django.contrib.auth.models import Group

# Register your models here.
# We regsiter our models here to use it with 127.0.0.8000/admin

from first_app.models import Topic,Entrie,TeamName,Mark,File
from django.contrib.contenttypes.admin import GenericTabularInline

admin.site.site_header = 'Student Database'
admin.site.site_title = 'Student Database'
#instead of side administration we changed it to student database
admin.site.index_title='Student Database'

"""
For dynamic users
"""
class TeamNameInline(GenericTabularInline):
    model = TeamName
    extra = 0
    min_num = 0

"""
For dynamic credit
"""
class MarkInline(GenericTabularInline):
    model = Mark
    extra = 0
    min_num = 1 

"""
For dynamic Files
"""
class FileInline(GenericTabularInline):
    model = File
    extra = 0 
    min_num = 0 

##############################################################


class EntriesAdmin(admin.ModelAdmin):
    list_filter = ('topics','department','year',)
    inlines = [
        TeamNameInline,
        MarkInline,
        FileInline,
    ]
    def get_queryset(self, request):
        qs = super(EntriesAdmin, self).get_queryset(request)
        username = request.user
        user_in_group = Group.objects.get(name="students").user_set.all()
        if username in user_in_group:
            return qs.filter(name=request.user)
        else:
             return qs
    
    # to view images inline
    def image_img(self):
        if self.File.file:
            return u'<img src ="%s"/>' % self.File.file.url
        else:
            return '(No file found)'
    image_img.short_description = 'Thumb'
    image_img.allow_tags = True
    

##############################################################




admin.site.register(Topic)
admin.site.register(Entrie,EntriesAdmin)

"""
Username : samyakgaur
Email Id: samyakgaur@yahoo.com
Password: @Samyak
"""

"""
Username : testuser
Email Id: NA
Password: @Samyakgaur
"""

from django.contrib import admin

# Register your models here.
# We regsiter our models here to use it with 127.0.0.8000/admin

from first_app.models import Topic,Entrie,TeamName,Mark
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

"""
For dynamic credit
"""
class MarkInline(GenericTabularInline):
    model = Mark

##############################################################


class EntriesAdmin(admin.ModelAdmin):
    list_filter = ('topics','department','year',)
    inlines = [
        TeamNameInline,
        MarkInline,
    ]


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

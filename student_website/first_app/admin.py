from django.contrib import admin

# Register your models here.
# We regsiter our models here to use it with 127.0.0.8000/admin

from first_app.models import Topic,Entries,TeamName
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

class EntriesAdmin(admin.ModelAdmin):
    inlines = [
        TeamNameInline,
    ]
##############################################################



admin.site.register(Topic)
admin.site.register(Entries,EntriesAdmin)

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

from django.contrib import admin
from django.contrib.auth.models import Group

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
    def get_queryset(self, request):
        qs = super(EntriesAdmin, self).get_queryset(request)
        username = request.user
        user_in_group = Group.objects.get(name="students").user_set.all()
        if username in user_in_group:
            return qs.filter(name=request.user)
        else:
             return qs

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

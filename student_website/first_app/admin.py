from django.contrib import admin

# Register your models here.
# We regsiter our models here to use it with 127.0.0.8000/admin

from first_app.models import Topic,Entries

admin.site.register(Topic)
admin.site.register(Entries)

"""
Username : samyakgaur
Email Id: samyakgaur@yahoo.com
Password: @Samyak
"""
"""student_website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
#we are importing views from our first app here 
from first_app import views 
# to map this with the urls.py file in first_app
from django.conf.urls import include

# for image url 

from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    #registering the url here
    path('first_app/',include('first_app.urls')),
    path('',views.index),
]

urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
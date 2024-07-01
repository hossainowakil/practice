
from django.contrib import admin
from django.urls import path
from masud.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home, name='home'),
    path('detail/<int:id>/',detail,name='detail')

]

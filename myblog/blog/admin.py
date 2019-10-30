from django.contrib import admin
from .models import Post



#add table created to the admin for easy accesibility
admin.site.register(Post)
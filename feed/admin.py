from django.contrib import admin
from .models import Post

# Here you would be able to see the models created in models.py, they would be viewable in the admin page dir

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    pass

admin.site.register(Post, PostAdmin)
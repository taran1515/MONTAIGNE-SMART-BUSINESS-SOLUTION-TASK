from django.contrib import admin
from .models import Post,Comment,Profile,Plan

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ('title','slug','author')
    list_filter = ('created',)

class CommentAdmin(admin.ModelAdmin):
    list_display = ('post','text')
    list_filter = ('created_date',)

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user','dob')



admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Profile,ProfileAdmin)
admin.site.register(Plan)

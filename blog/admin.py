from django.contrib import admin


from .models import BlogPost, Image


class ImageInline(admin.TabularInline):
    model=Image



class BlogPostAdmin(admin.ModelAdmin):
    inlines=[ImageInline]
    list_display=["title","post_type"]

admin.site.register(BlogPost,BlogPostAdmin)


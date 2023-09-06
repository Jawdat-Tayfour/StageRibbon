from django.db import models
from django.urls import reverse
import uuid
from ckeditor.fields import RichTextField



class BlogPost(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4)
    cover_url = models.URLField(blank=True,null=True)
    video_url = models.URLField(blank=True,null=True)
    title = models.TextField(max_length=150)
    body = RichTextField(max_length=8000)
    post_type=models.CharField(max_length=50)
    latest = models.BooleanField(blank=True,default=False)
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse("post_detail", args=[str(self.id)])    
    

    


class Image(models.Model):
    post = models.ForeignKey(BlogPost, related_name="images", on_delete=models.CASCADE)
    image = models.URLField(blank=True)






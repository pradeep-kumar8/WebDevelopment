from django.db import models
from tinymce.models import HTMLField


# add blog
class Services(models.Model):
    blog_title = models.CharField(max_length=50)
    # blog_desc=models.TextField()
    blog_desc = HTMLField()
    # auto_slug=AutoSlugField(populate_from=blog_title, unique=True, null=True, default=None)


# These field required contact to us (footer) data
class Ctu(models.Model):
    Name = models.CharField(max_length=50)
    Dob = models.DateTimeField()
    Email = models.EmailField()
    Phone = models.CharField(max_length=13)
    File = models.FileField(upload_to='file/', max_length=250, null=True, default=None)

    # Print Name as title in database in admin panel
    def __str__(self):
        return self.Name


# These field required about us data
class About(models.Model):
    Name = models.CharField(max_length=50)
    Email = models.EmailField()
    Phone = models.CharField(max_length=13)
    Textarea = models.TextField(max_length=500)

    def __str__(self):
        return self.Name

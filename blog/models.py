from django.db import models
from django.template.defaultfilters import slugify

# Create your models here.
class Post(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)
    title = models.CharField(max_length = 140)
    slug = models.SlugField(max_length=255,blank=True, default='')
    body = models.TextField()
    published = models.BooleanField(default=True)

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Post, self).save(*args,**kwargs)
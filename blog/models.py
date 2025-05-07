from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=200)
    main_content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    img = models.ImageField(upload_to='images')
    slug = models.SlugField(null=False, blank=True)

    def __str__(self):
        return f'{self.title}'
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)
    
    def get_absolute_url(self):
        return reverse("post-detail-page", kwargs={"slug": self.slug})
    
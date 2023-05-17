import datetime

from django.db import models
from django.utils.text import slugify
from users.models import User


class Tag(models.Model):
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True, null=True, blank=True)

    def __str__(self):
        return self.name

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if self.name.upper():
            self.slug = slugify(self.name.lower())
        return super().save(force_insert, force_update, using, update_fields)


class Post(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=255, )
    text = models.TextField(null=True, blank=True)
    tags = models.ManyToManyField('Tag', related_name='posts')
    author = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE, blank=True, null=True)
    image = models.ImageField(upload_to='images', null=True, blank=True)
    pub_year = datetime.datetime.now().strftime("%H:%M / %d.%m.%Y")
    video = models.FileField(upload_to='video', null=True, blank=True)
    category = models.ForeignKey("Category", on_delete=models.CASCADE, related_name="category")
    liked = models.ManyToManyField(User, related_name='liked', )

    def __str__(self):
        return self.title

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if self.title.upper():
            self.slug = slugify(self.title.lower())
        return super().save(force_insert, force_update, using, update_fields)


class Category(models.Model):
    name = models.CharField(max_length=255, unique=True, null=True)
    slug = models.SlugField(max_length=255, unique=True, blank=True, null=True)

    def __str__(self):
        return self.name

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if self.name.upper():
            self.slug = slugify(self.name.lower())
        return super().save(force_insert, force_update, using, update_fields)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='replies')
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ('created_at',)

    def __str__(self):
        return f'Comment by {self.author.username} on {self.post}'

    def children(self):
        return Comment.objects.filter(parent=self)

    @property
    def is_parent(self):
        if self.parent is not None:
            return False
        return True

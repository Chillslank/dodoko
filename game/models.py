from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify, urlencode


class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)


    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

class Page(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=128)
    url = models.URLField()
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    picture = models.ImageField(upload_to='game_images', blank=True)
    describe = models.TextField()
    rate = models.CharField(max_length=128)

    def __str__(self):
        return self.title

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)

    def __str__(self):
        return self.user.username

class Comment(models.Model):
    user = models.CharField(max_length=128)
    page = models.ForeignKey(Page, on_delete=models.CASCADE)
    content = models.TextField()
    posttime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user

class WishList(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    page = models.CharField(max_length=128)
    url = models.URLField()

    def __str__(self):
        return self.user

class Operation():
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    event = models.CharField(max_length=128)
    time = models.DateTimeField()

    def __str__(self):
        return self.event
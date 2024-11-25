from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):
    CATEGORY_CHOICE = (
        ('b', 'Builds'),
        ('w', 'Weapons'),
        ('s', 'Stats'),
        ('o', 'Other'),
    )
    title = models.CharField(max_length=200)
    picture = models.ImageField(upload_to=None, height_field=None,width_field=None)
    body = models.TextField()
    created_on = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=0)
    likes = models.ManyToManyField(User, blank=True, related_name='likes')
    category =  models.CharField(max_length=1 ,choices=CATEGORY_CHOICE, default='o')


class Comment(models.Model):
    comment = models.TextField()
    created_on = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=0)
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, blank=True, related_name='comment_likes')
    parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, related_name='+')
    
    @property
    def children(self):
        return Comment.objects.filter(parent=self).order_by('-created_on').all()
    
    @property
    def is_parent(self):
        if self.parent is None:
            return True
        return False
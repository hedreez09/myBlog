from django.db import models
from django.conf import settings
from django.utils  import timezone

#create=ing a post method to create tables in the database
class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length = 200)
    text = models.TextField()
    created_date = models.DateTimeField(default = timezone.now)
    published_data = models.DateTimeField(blank =True, null = True)


#to publish the time zone
    def publish(self):
        sel.published_data = timezone.now()
        self.save()

#return title of the post
    def __str__(self):
        return self.title
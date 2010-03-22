from django.db import models


class Feed(models.Model):
    url = models.URLField()
    last_update = models.DateTimeField(blank=True, null=True)

    def __unicode__(self):
        return self.url


class Entry(models.Model):
    author = models.CharField(max_length=100)
    title = models.CharField(max_length=500)
    link = models.URLField()
    updated = models.DateTimeField()
    html = models.TextField()

    def __unicode__(self):
        return '%s - %s' % (self.author, self.title)

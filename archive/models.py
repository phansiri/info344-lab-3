from django.db import models

class urlSites(models.Model):
    owner = models.ForeignKey('auth.User', related_name='archive')
    originalUrl = models.URLField()
    finalUrl = models.URLField(blank=True)
    httpStatusCode = models.CharField(blank=True, max_length=5)
    pageTitle = models.CharField(blank=True, max_length=400)
    screenShot = models.URLField(blank=True)

    def submit(self):
        self.save()

    def save(self, *args, **kwargs):
        super(urlSites, self).save(*args, **kwargs)

    def __str__(self):
        return self.originalUrl

from django.db import models


class AboutUs(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    # image = models.ImageField(upload_to='about_us/')

    def __str__(self):
        return self.title


class WhyChooseUs(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()

    def __str__(self):
        return self.title


class Chef(models.Model):
    name = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    bio = models.TextField()
    image = models.ImageField(upload_to='chef/')

    def __str__(self):
        return self.name

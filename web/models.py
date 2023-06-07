from django.db import models



class Subscribe(models.Model):
    email = models.EmailField(max_length=255) 

    def __str__(self):
        return self.email


class Customer(models.Model):
    image = models.FileField(upload_to="cusomer", max_length=255)


    def __str__(self):
        return self.image.name

class Feature(models.Model):
    image = models.ImageField(upload_to="feature")
    icon = models.FileField(upload_to="feature", max_length=255)
    icon_background = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    description = models.TextField()
    testimonial_description = models.TextField()
    testimonial_author = models.CharField(max_length=255)
    author_designation = models.CharField(max_length=255)
    testimonial_logo = models.FileField(upload_to="feature", max_length=255)


    def __str__(self):
        return self.testimonial_logo.name
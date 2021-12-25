from django.db import models

# Create your models here.

class AboutUs(models.Model):
    title = models.CharField(max_length=250)
    desc = models.TextField()
    image = models.ImageField(upload_to=None)
    

    class Meta:
        verbose_name = ("AboutUs")
        verbose_name_plural = ("AboutUss")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("AboutUs_detail", kwargs={"pk": self.pk})


class ContactUs(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    phone = models.PhoneNumberField()
    subject = models.CharField(max_length=250)
    text = models.TextField()
    

    class Meta:
        verbose_name = ("ContactUs")
        verbose_name_plural = ("ContactUss")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("ContactUs_detail", kwargs={"pk": self.pk})

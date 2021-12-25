from django.db import models

# Create your models here.

class Service(models.Model):
    name = models.CharField(max_length=150)
    icon = models.CharField(max_length=150)
    desc = models.TextField()
    

    class Meta:
        verbose_name = ("Service")
        verbose_name_plural = ("Services")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Service_detail", kwargs={"pk": self.pk})

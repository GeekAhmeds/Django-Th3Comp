from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=150)
    image = models.ImageField(blank=True, upload_to=None)
    

    class Meta:
        verbose_name = ("Category")
        verbose_name_plural = ("Categories")

    def __str__(self):
        return self.name



class Blog(models.Model):
    title = models.CharField(max_length=250)
    image = models.ImageField(upload_to=None)
    Author = models.ForeignKey(User, verbose_name=("Author"), on_delete=models.CASCADE)
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now=True)
    Category = models.ForeignKey(Category, verbose_name=("Category"), on_delete=models.CASCADE)
#    tag =
#    comment = 


    class Meta:
        verbose_name = ("Blog")
        verbose_name_plural = ("Blogs")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("Blog_detail", kwargs={"pk": self.pk})

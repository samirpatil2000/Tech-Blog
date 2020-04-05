from PIL import Image
from django.db import models

# Create your models here.
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User


class Category(models.Model):
    id_of_cat=models.AutoField
    title = models.CharField(max_length=20)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('cat-posts', kwargs={'id': self.pk})


class Post(models.Model):
    id_of_post=models.AutoField
    title=models.CharField(max_length=100)
    content=models.TextField()
    date_posted=models.DateTimeField(default=timezone.now())
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category)
    thumbnail=models.ImageField()
    #featured=models.BooleanField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-details',kwargs={'id':self.pk})

    @property
    def view_count(self):
        return PostView.objects.filter(post=self).count()



    #
    # def save(self,*args,**kwargs):
    #     super().save(*args,**kwargs)
    #     thumbnail=Image.open(self.thumbnail.path)
    #     if thumbnail.height > 300 or thumbnail.width > 300 :
    #         output_size=(200,200)
    #         thumbnail.thumbnail(output_size)
    #         thumbnail.save(self.thumbnail.path)
    #    # img_1=Image.open(self.blog_image.path)
    #     img_2=Image.open(self.blog_image_1.path)
    #     #
    #     #
    #     # if img_1.height > 400 or img_1.width > 400 or img_2.height > 400 or img_2.width > 400 :
    #     #     output_size=(400,400)
    #     #     img_1.thumbnail(output_size)
    #     #     img_2.thumbnail(output_size)
    #     #     img_1.save(self.blog_image.path)
    #     #     img_2.save(self.blog_image_1.path)
    #

class PostView(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    post=models.ForeignKey(Post,on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
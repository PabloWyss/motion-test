from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Post(models.Model):
    text = models.TextField()
    like_count = models.IntegerField(default=0, blank=True)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
    created_by = models.ForeignKey(to=User, on_delete=models.PROTECT, related_name="posts")
    liked_by = models.ManyToManyField(to=User, related_name="posts_liked", blank=True)
    followed_by = models.ManyToManyField(to=User, related_name="posts_followed", blank=True)

    # def save(self, *args, **kwargs):
    #     self.like_count = len(self.liked_by.all())
    #     super().save(*args, **kwargs)  # Call the "real" save() method.
    #
    # def len_num(self):
    #     self.save()

    def __str__(self):
        return f'{self.id} - Post text {self.text}'

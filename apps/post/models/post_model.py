from django.db import models

from apps.common import BaseModel


class Post(BaseModel):
    owner = models.ForeignKey("user.User", on_delete=models.CASCADE, related_name="posts")

    description = models.TextField()
    location = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return f"{self.owner.username}"

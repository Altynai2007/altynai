from django.db import models


class Announcement(models.Model):
    title = models.CharField(max_length=155)
    description = models.TextField()
    main_image = models.ImageField(upload_to="images/announcement/")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('created_at', ) 

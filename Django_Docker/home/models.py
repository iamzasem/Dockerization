from django.db import models

class AlbumCategory(models.Model):
    name = models.CharField(max_length=100)
    cover_image = models.ImageField(upload_to='album_covers/', blank=True, null=True)
    
    def __str__(self):
        return self.name

class Photo(models.Model):
    album = models.ForeignKey(AlbumCategory, on_delete=models.CASCADE, related_name='photos')
    title = models.CharField(max_length=100, blank=True)
    image = models.ImageField(upload_to='photos/')
    
    def __str__(self):
        return self.title or f"Photo in {self.album}"

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
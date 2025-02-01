from django.db import models
from django.contrib.auth import get_user_model

class Destination(models.Model):
    CITIES = [
        ('BERN', 'Bern, Switzerland'),
        ('BRAS', 'Brasília, Brazil'),
        ('HK', 'Hong Kong, China'),
        ('SYD', 'Sydney, Australia'),
        ('NYC', 'New York, USA'),
        ('ACC', 'Accra, Ghana')
    ]

    city = models.CharField(max_length=4, choices=CITIES)
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='destinations/')
    popup_image = models.ImageField(upload_to='destinations/', null=True, blank=True) 
    landmarks = models.TextField()
    activities = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.get_city_display()
    
class Comment(models.Model):
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    text = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_on']
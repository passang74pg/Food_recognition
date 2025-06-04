from django.db import models
from django.utils import timezone

class FoodPrediction(models.Model):
    image = models.ImageField(upload_to='uploads/')
    predicted_class = models.CharField(max_length=100)
    confidence = models.FloatField()
    timestamp = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return f"{self.predicted_class} - {self.confidence:.2f}%"
    
    class Meta:
        ordering = ['-timestamp']
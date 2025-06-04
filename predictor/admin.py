from django.contrib import admin
from .models import FoodPrediction

@admin.register(FoodPrediction)
class FoodPredictionAdmin(admin.ModelAdmin):
    list_display = ['predicted_class', 'confidence', 'timestamp']
    list_filter = ['predicted_class', 'timestamp']
    search_fields = ['predicted_class']
    readonly_fields = ['timestamp']
    ordering = ['-timestamp']
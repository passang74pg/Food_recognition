from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
import os

# Load model once at the top
model = load_model(os.path.join('my_model.keras'))

# Define your class labels (adjust as per your dataset)
class_labels = ['chocolate_cake','dumplings','fried_rice', 'pizza', 'waffles']

def index(request):
    context = {}
    if request.method == 'POST' and request.FILES['food_image']:
        uploaded_file = request.FILES['food_image']
        fs = FileSystemStorage()
        file_path = fs.save(uploaded_file.name, uploaded_file)
        full_path = fs.url(file_path)
        
        # Load and preprocess image
        img_path = os.path.join('media', file_path)
        img = image.load_img(img_path, target_size=(224, 224))  # adjust size if needed
        img_array = image.img_to_array(img)
        img_array = np.expand_dims(img_array, axis=0) / 255.0
        
        # Predict
        predictions = model.predict(img_array)
        predicted_class = class_labels[np.argmax(predictions[0])]
        confidence = float(np.max(predictions[0]))
        
        context = {
            'uploaded_file_url': full_path,
            'predicted_class': predicted_class,
            'confidence': f"{confidence * 100:.2f}%"
        }
    
    return render(request, 'predictor/index.html', context)

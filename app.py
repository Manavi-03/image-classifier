# app.py
from flask import Flask, request, render_template, jsonify
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
import os

app = Flask(__name__)
model = load_model('mobilenet_classifier.h5')

# Class labels + emoji
class_labels = {
    'cardboard': '📦 Cardboard',
    'glass': '🧪 Glass',
    'metal': '🥢 Metal',
    'paper': '📄 Paper',
    'plastic': '🧴 Plastic',
    'trash': '🚮 Trash'
}

# Bin recommendations + emoji
bin_map = {
    'cardboard': 'Blue Box ♻️',
    'glass': 'Blue Box ♻️',
    'metal': 'Blue Box ♻️',
    'paper': 'Blue Box ♻️',
    'plastic': 'Blue Box ♻️',
    'trash': 'Black Bin 🗑️'
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'Empty filename'}), 400

    upload_folder = 'static/uploads'
    os.makedirs(upload_folder, exist_ok=True)
    img_path = os.path.join(upload_folder, file.filename)
    file.save(img_path)

    img = image.load_img(img_path, target_size=(224, 224))
    img_array = image.img_to_array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    predictions = model.predict(img_array)
    predicted_index = np.argmax(predictions[0])
    predicted_class_key = list(class_labels.keys())[predicted_index]
    predicted_label = class_labels[predicted_class_key]
    confidence = float(np.max(predictions[0]))
    bin_type = bin_map[predicted_class_key]

    return jsonify({
        'label': predicted_label,
        'confidence': round(confidence * 100, 2),
        'bin': bin_type
    })

if __name__ == '__main__':
    app.run(debug=True)






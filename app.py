import os
from flask import Flask, request, render_template
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import load_img, img_to_array
import numpy as np
import io

app = Flask(__name__)

# Define the labels
labels = {0: 'Corn__common_rust',
 1: 'Corn__gray_leaf_spot',
 2: 'Corn__healthy',
 3: 'Corn__northern_leaf_blight',
 4: 'Potato__early_blight',
 5: 'Potato__healthy',
 6: 'Potato__late_blight',
 7: 'Soybean__bacterial_blight',
 8: 'Soybean__caterpillar',
 9: 'Soybean__diabrotica_speciosa',
 10: 'Soybean__downy_mildew',
 11: 'Soybean__healthy',
 12: 'Soybean__mosaic_virus',
 13: 'Soybean__powdery_mildew',
 14: 'Soybean__rust',
 15: 'Soybean__southern_blight',
 16: 'Tomato__bacterial_spot',
 17: 'Tomato__early_blight',
 18: 'Tomato__healthy',
 19: 'Tomato__late_blight',
 20: 'Tomato__leaf_mold',
 21: 'Tomato__mosaic_virus',
 22: 'Tomato__septoria_leaf_spot',
 23: 'Tomato__spider_mites_(two_spotted_spider_mite)',
 24: 'Tomato__target_spot',
 25: 'Tomato__yellow_leaf_curl_virus'}

def preprocess_image(image, target_size=(225, 225)):
    img = load_img(io.BytesIO(image), target_size=target_size)
    x = img_to_array(img)
    x = x.astype('float32') / 255.
    x = np.expand_dims(x, axis=0)
    return x

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return 'No file uploaded', 400

    file = request.files['file']

    if file.filename == '':
        return 'No file selected', 400

    image = file.read()
    x = preprocess_image(image)
    predictions = model.predict(x)
    predicted_index = np.argmax(predictions)

    if predicted_index in labels:
        predicted_label = labels[predicted_index]
    else:
        predicted_label = 'Unknown class'

    return predicted_label

if __name__ == '__main__':
    # Load the model from the local file
    model = load_model('main_model.h5')

    app.run(debug=True)
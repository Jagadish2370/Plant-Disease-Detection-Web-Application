# 🌱 Plant Disease Detection
![pl](https://github.com/user-attachments/assets/1571d79e-fd16-496b-9ad2-e2b5d720f48a)


## 🔍 Overview
This project is a **Plant Disease Detection** web application using Flask and a deep learning model. Users can upload plant leaf images, and the model will classify the disease based on the given categories.

## ⭐ Features
- Accepts image uploads for prediction.
- Uses a pre-trained deep learning model (`main_model.h5`) for classification.
- Categorizes plant diseases across **Corn, Potato, Soybean, and Tomato** plants.
- Provides a web interface for easy interaction.

## 🧩 Dependencies
- Flask
- TensorFlow / Keras
- NumPy
- Pillow

## 🛠 Installation

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Ensure `main_model.h5` is present in the project directory.

3. Run the application:
   ```bash
   python app.py
   ```

4. Access the web app at:
   ```
   http://127.0.0.1:5000/
   ```

## 📂 File Structure
```
/project-root
│── app.py                # Flask application
│── main_model.h5         # Trained deep learning model
│── templates/
│   └── index.html        # Webpage template
│── static/               # CSS, JS, Images (if any)
│── requirements.txt      # Python dependencies
│── README.md             # Documentation
```

## ⚙️ How It Works
1. User uploads an image via the web interface.
2. The image is preprocessed and fed into the trained model.
3. The model predicts the disease category.
4. The result is displayed to the user.

## 🌾 Supported Plant Diseases
The model supports classification of 26 categories, including:
- **Corn:** Common rust, gray leaf spot, northern leaf blight, healthy
- **Potato:** Early blight, late blight, healthy
- **Soybean:** Bacterial blight, mosaic virus, rust, healthy, etc.
- **Tomato:** Early blight, bacterial spot, mosaic virus, spider mites, etc.

## 📊 Project Output
Upon successful image upload and processing, the application will display:
- The detected plant disease.
![image](https://github.com/user-attachments/assets/5df3b9f1-cfeb-4385-acb2-e1a9f49f430b)
![image](https://github.com/user-attachments/assets/1e7fe0a0-df65-460f-ad58-df95db082402)








# 🧠 Waste Classifier with Smart Bin Recommendation ♻️

This is a **deep learning web app** that classifies an image of waste (plastic, glass, metal, cardboard, paper, or trash) and recommends the appropriate disposal bin based on **Ontario’s blue/black bin system**. Users can drag and drop an image, and the app will instantly return a prediction with emoji-labeled feedback, confidence level, and disposal instructions.


---

## 📸 Example Output
![App Screenshot](ss1.png)


---

## 🧰 Tech Stack

| Technology        | Purpose                                    |
|------------------|---------------------------------------------|
| Python            | Core backend logic                         |
| Flask             | Web framework for handling routes and APIs |
| HTML/CSS/JS       | Frontend UI with drag-and-drop support     |
| TensorFlow/Keras  | Deep learning model (MobileNet-based)      |
| NumPy             | Image preprocessing                        |

---

## 📦 Waste Categories Recognized

- 📦 Cardboard → Blue Box ♻️  
- 🧪 Glass → Blue Box ♻️  
- 🥢 Metal → Blue Box ♻️  
- 📄 Paper → Blue Box ♻️  
- 🧴 Plastic → Blue Box ♻️  
- 🚮 Trash → Black Bin 🗑️  

---

## 📊 Model Accuracy

- **Model:** MobileNetV2 (transfer learning)
- **Input Size:** 224x224 pixels
- **Final Accuracy:** ~60% (significantly improved from baseline ~22%)
- **Performance Notes:**
  - Cardboard and Paper → consistently accurate
  - Glass ↔️ Plastic → occasional misclassifications
  - Trash → more distinct when image is clear

---

🧾 **Confusion Matrix**  
*(To be added)*  
![Confusion Matrix](confusionmatrix.png)





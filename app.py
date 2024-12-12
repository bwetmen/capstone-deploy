from fastapi import FastAPI, UploadFile, HTTPException
from fastapi.responses import JSONResponse
import numpy as np
import os
from sklearn.metrics import classification_report, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import ImageDataGenerator

app = FastAPI()

# Konfigurasi model dan path
MODEL_PATH = "model"
MODEL_FILE = os.path.join(MODEL_PATH, "model.h5")
CONFUSION_MATRIX_FILE = os.path.join(MODEL_PATH, "confusion_matrix.png")

# Load model
if not os.path.exists(MODEL_FILE):
    raise FileNotFoundError(f"Model file not found at {MODEL_FILE}")

model = load_model(MODEL_FILE)

@app.post("/predict")
async def predict(file: UploadFile):
    """API untuk memprediksi hasil klasifikasi menggunakan model terlatih."""
    # Validasi input file
    if not file.filename.endswith(".zip"):
        raise HTTPException(status_code=400, detail="Input file must be a .zip archive containing images.")

    # Proses file input (contoh: Anda perlu mengekstrak file di sini dan mempersiapkan data)
    # Misalnya, simpan dan proses data di direktori sementara:
    TEMP_DIR = "temp_test_data"
    if os.path.exists(TEMP_DIR):
        import shutil
        shutil.rmtree(TEMP_DIR)
    os.makedirs(TEMP_DIR, exist_ok=True)

    file_location = os.path.join(TEMP_DIR, file.filename)
    with open(file_location, "wb") as f:
        f.write(await file.read())

    # Ekstraksi file (jika format zip)
    import zipfile
    with zipfile.ZipFile(file_location, 'r') as zip_ref:
        zip_ref.extractall(TEMP_DIR)

    # Konfigurasi ImageDataGenerator
    test_datagen = ImageDataGenerator(rescale=1.0/255.0)
    test_generator = test_datagen.flow_from_directory(
        TEMP_DIR,
        target_size=(224, 224),  # Sesuaikan ukuran gambar dengan model Anda
        batch_size=32,
        class_mode="categorical",
        shuffle=False
    )

    # Reset test generator untuk memastikan konsistensi
    test_generator.reset()

    # Prediksi pada test set
    predictions = model.predict(test_generator)
    predicted_classes = np.argmax(predictions, axis=1)

    # Dapatkan true labels
    true_classes = test_generator.classes
    class_labels = list(test_generator.class_indices.keys())

    # Validasi panjang array
    if len(true_classes) != len(predicted_classes):
        raise HTTPException(status_code=500, detail="Mismatch between true and predicted class lengths.")

    # Classification report
    classification_report_dict = classification_report(true_classes, predicted_classes, target_names=class_labels, output_dict=True)

    # Confusion Matrix
    cm = confusion_matrix(true_classes, predicted_classes)
    plt.figure(figsize=(10, 7))
    sns.heatmap(cm, annot=True, fmt='g', cmap='Blues', xticklabels=class_labels, yticklabels=class_labels)
    plt.xlabel('Predicted')
    plt.ylabel('Actual')
    plt.title('Confusion Matrix')
    plt.xticks(rotation=45, ha='right')
    plt.yticks(rotation=45)
    plt.tight_layout()
    plt.savefig(CONFUSION_MATRIX_FILE)
    plt.close()

    # Tampilkan metrik per kelas
    class_metrics = {}
    for i, class_name in enumerate(class_labels):
        class_predictions = predicted_classes == i
        class_true = true_classes == i
        class_accuracy = np.sum(class_predictions & class_true) / np.sum(class_true)
        class_metrics[class_name] = {
            "accuracy": round(class_accuracy, 4)
        }

    # Buat respons JSON
    response = {
        "classification_report": classification_report_dict,
        "class_metrics": class_metrics,
        "confusion_matrix": f"Confusion matrix saved to {CONFUSION_MATRIX_FILE}"
    }

    return JSONResponse(content=response)

@app.get("/health")
async def health_check():
    """API untuk memeriksa status layanan."""
    return {"status": "ok", "message": "Service is running"}

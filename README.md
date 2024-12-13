# Skin Health Analysis Project

This project is a web-based application that analyzes skin health by uploading images and provides recommendations based on the analysis. The project is implemented using **FastAPI** for the backend and **HTML/CSS/JavaScript** for the frontend.

---

## Features

1. **Skin Health Analysis**:
   - Upload skin images to get instant analysis.
   - Backend processes the images and returns results.
2. **Search Functionality**:
   - Easily navigate the website sections using the search bar.
3. **Interactive Cards**:
   - Displays interactive cards for "FATISDA".
4. **Real-Time Date Display**:
   - A button to display the current date and time.
5. **Loading Indicator**:
   - Shows a spinner while analyzing images.

---

## Prerequisites

### Backend:
- **Python** (>= 3.8)
- **FastAPI**
- **Uvicorn**

Install dependencies:
```bash
pip install -r requirements.txt
```

### Frontend:
- HTML
- CSS
- JavaScript (jQuery included)

---

## How to Run the Project

### Backend:
1. Clone the repository:
   ```bash
   git clone <repository_url>
   ```
2. Navigate to the project directory and start the server:
   ```bash
   uvicorn app:app --reload
   ```
3. The server will run on [http://127.0.0.1:8000](http://127.0.0.1:8000).
4. Access the interactive API documentation at [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs).

### Frontend:
1. Navigate to the `static` directory.
2. Open the `index.html` file in your preferred browser.
3. Ensure the backend server is running and accessible.

---

## Project Structure

```
.
├── ALSkindetecML
│   ├── __pycache__               # Python bytecode cache
│   ├── envScriptsactivate        # Virtual environment setup files
│   ├── model                     # Machine learning models
│   ├── static                    # Frontend files
│   │   ├── images                # Image assets
│   │   ├── index.html            # Main HTML file
│   │   ├── script.js             # JavaScript functionality
│   │   └── style.css             # Stylesheet for the application
│   ├── temp_test_data            # Temporary test data for the models
│   ├── app.py                    # FastAPI application
│   ├── requirements.txt          # Backend dependencies
│   ├── ensemble_model.h5         # Trained ensemble model
│   ├── skin_disease_model        # Additional model files
│   ├── CNN\_SkinDiseaseTfLite    # TensorFlow Lite model (if applicable)
│   ├── ConfusionMatrix.png       # Performance visualization
│   ├── graph.png                 # Model accuracy/loss graph
│   ├── README-cloudshell.txt     # Cloudshell instructions
│   └── README.md                 # Project documentation
```

---

## API Endpoints

### Upload Image
- **Endpoint**: `POST /upload-image/`
- **Description**: Uploads an image for analysis.
- **Request**:
  - Form data with a file field named `file`.
- **Response**:
  ```json
  {
   {
  "predicted_label": "Eczema",
  "confidence": 0.8531
}
  }
  ```

---

## Troubleshooting

1. **CORS Errors**:
   - Ensure the backend allows requests from the frontend's domain.
   - Modify `allow_origins` in `app.py` to include your frontend URL.

2. **No Analysis Display**:
   - Check if the backend server is running.
   - Open the browser console (F12) and inspect network or JavaScript errors.

3. **File Not Found**:
   - Verify that the uploaded file meets the requirements.
   - Ensure the `accept="image/*"` attribute is present in the `<input>` tag.

---

## Contributions
Contributions are welcome! Feel free to fork the repository and submit a pull request with your improvements.

---

## License
This project is licensed under the [MIT License](LICENSE).

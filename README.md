# anpr
# Automatic Number Plate Recognition (ANPR) System

This project is a real-time **Automatic Number Plate Recognition (ANPR)** system developed using **Python**, **OpenCV**, and **Tesseract OCR**. It detects license plates from live video streams, localizes the plate area, and optionally extracts the alphanumeric content.

## 🚀 Features

- Real-time license plate detection
- Edge and contour analysis for plate localization
- Bounding box visualization
- Optional OCR for character extraction
- Adaptable to varied lighting conditions
- Scalable and efficient system
- Optional database integration for verification

## 🧠 Technologies Used

- Python
- OpenCV
- NumPy
- Tesseract OCR (optional for text recognition)

> ⚠️ Install Tesseract OCR separately from https://github.com/tesseract-ocr/tesseract

## 🛠️ How It Works

1. Captures live video using a webcam or surveillance camera.
2. Pre-processes the frame (grayscale, blur, edge detection).
3. Detects contours and filters them by aspect ratio.
4. Localizes the license plate area.
5. Optionally extracts and displays the number using OCR.
6. Optionally compares results with a database (e.g., for stolen vehicles).

## 📸 Output

- Bounding box around detected number plate.
- Real-time feedback: shows the detected area or "Scanning for Plate..." message.

## ▶️ Usage

```bash
python anpr_system.py
```

Press `q` to exit the live feed.

## 📂 Project Structure

```
.
├── anpr_system.py       # Main detection script
├── README.md            # Project overview
```

## ✍️ Authors

- Kishore Kumar R
- Jebin S
- Antony Basta Satheesh S
- Ashin D

## 📌 Future Enhancements

- Integrate Tesseract OCR for complete plate recognition
- Add database matching features
- Improve detection with deep learning models

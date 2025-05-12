import cv2
import numpy as np

# Start webcam capture
camera = cv2.VideoCapture(0)
camera.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

while True:
    ret, frame = camera.read()
    if not ret:
        break

    # Resize and grayscale conversion
    frame_resized = cv2.resize(frame, (640, 480))
    gray = cv2.cvtColor(frame_resized, cv2.COLOR_BGR2GRAY)

    # Apply Gaussian blur
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    # Edge detection
    edged = cv2.Canny(blurred, 50, 200)

    # Detect contours
    contours, _ = cv2.findContours(edged, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contours = sorted(contours, key=cv2.contourArea, reverse=True)[:15]

    plate_found = False

    for contour in contours:
        approx = cv2.approxPolyDP(contour, 0.018 * cv2.arcLength(contour, True), True)

        if len(approx) == 4:
            x, y, w, h = cv2.boundingRect(approx)
            ratio = w / float(h)

            if 2.0 < ratio < 6.0 and w > 120 and h > 30:
                plate_found = True
                cv2.drawContours(frame_resized, [approx], -1, (0, 255, 0), 2)
                cv2.putText(frame_resized, "License Plate", (x, y - 10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

                plate_image = frame_resized[y:y + h, x:x + w]
                cv2.imshow("Detected Plate", plate_image)
                break

    if not plate_found:
        cv2.putText(frame_resized, "Scanning for Plate...", (20, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (100, 100, 255), 2)

    cv2.imshow("ANPR - Live Feed", frame_resized)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

camera.release()
cv2.destroyAllWindows()


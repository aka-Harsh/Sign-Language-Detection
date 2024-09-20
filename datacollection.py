import cv2
from cvzone.HandTrackingModule import HandDetector
import numpy as np
import math
import time

# Corrected file path with raw string to avoid invalid escape sequences
folder = r"C:\Projects\Sign\data\I_love_you"

cap = cv2.VideoCapture(0)
detector = HandDetector(maxHands=1)  # Detect only one hand at a time
offset = 20
imgSize = 500
counter = 0

while True:
    success, img = cap.read()
    if not success:
        break

    # Detect hand in the frame
    hands, img = detector.findHands(img)
    if hands:
        hand = hands[0]
        x, y, w, h = hand['bbox']

        # Create a white background image
        imgWhite = np.ones((imgSize, imgSize, 3), np.uint8) * 255

        # Adjust crop region to ensure it doesn't go out of bounds
        y1 = max(0, y - offset)
        y2 = min(img.shape[0], y + h + offset)
        x1 = max(0, x - offset)
        x2 = min(img.shape[1], x + w + offset)

        imgCrop = img[y1:y2, x1:x2]

        if imgCrop.size != 0:  # Only proceed if imgCrop is not empty
            # Calculate aspect ratio of hand region
            aspectRatio = h / w

            if aspectRatio > 1:  # If height > width
                k = imgSize / h
                wCal = math.ceil(k * w)
                imgResize = cv2.resize(imgCrop, (wCal, imgSize))
                wGap = math.ceil((imgSize - wCal) / 2)
                
                # Fix for size mismatch: clip if imgResize exceeds bounds
                if imgResize.shape[1] > imgSize:
                    imgResize = imgResize[:, :imgSize]  # Clip width if it's too large

                imgWhite[:, wGap:wCal + wGap] = imgResize

            else:  # If width >= height
                k = imgSize / w
                hCal = math.ceil(k * h)
                imgResize = cv2.resize(imgCrop, (imgSize, hCal))
                hGap = math.ceil((imgSize - hCal) / 2)
                
                # Fix for size mismatch: clip if imgResize exceeds bounds
                if imgResize.shape[0] > imgSize:
                    imgResize = imgResize[:imgSize, :]  # Clip height if it's too large

                imgWhite[hGap:hCal + hGap, :] = imgResize

            # Show the cropped and processed images
            cv2.imshow('ImageCrop', imgCrop)
            cv2.imshow('ImageWhite', imgWhite)

    # Show the original webcam feed
    cv2.imshow('Image', img)

    # Save the image when 's' key is pressed
    key = cv2.waitKey(1)
    if key == ord("s"):
        counter += 1
        # Save the image with timestamp in the folder
        cv2.imwrite(f'{folder}/Image_{time.time()}.jpg', imgWhite)
        print(f"Image saved: {counter}")

# Release the video capture and close windows
cap.release()
cv2.destroyAllWindows()


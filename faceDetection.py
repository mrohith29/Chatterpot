import cv2

# Load the cascade
data = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# To capture video from webcam
cap = cv2.VideoCapture(0)

while True:
    # Read the frame
    _, image = cap.read()

    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imshow('gray', gray)

    # Detect the faces
    faces = data.detectMultiScale(gray, 1.1, 4)

    # Draw the rectangle around each face
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x+w, y+h), (43, 226, 131), 4)

    # Display
    # cv2.imshow('image', image)
    # gray = data.detectMUltiScale(gray, 1.1, 4)
    cv2.imshow('image', image)
    cv2.inRange(image, (0, 0, 0), (255, 255, 255), gray)

    # Stop if escape key is pressed
    k = cv2.waitKey(30)
    if k==27:
        break

# Release the VideoCapture object
cap.release()
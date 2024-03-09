from fer import FER
import cv2

# Create a FER object
detector = FER()

# Open the webcam
cap = cv2.VideoCapture(0)

while True:
    # Read a frame from the webcam
    ret, frame = cap.read()

    # If a frame was successfully read
    if ret:
        # Detect emotions in the frame
        result = detector.detect_emotions(frame)

        # For each detected face
        for i in result:
            # Get the bounding box and emotions
            box = i["box"]
            emotions = i["emotions"]

            # Draw a rectangle around the face
            cv2.rectangle(frame, (box[0], box[1]), (box[0] + box[2], box[1] + box[3]), (0, 255, 0), 2)

            # Print the emotions
            print(emotions)

        # Display the frame
        cv2.imshow("Emotion Detection", frame)

        # If 'q' is pressed, stop the loop
        if cv2.waitKey(1):# & 0xFF == ord('q'):
            break

# Release the webcam and destroy all windows
cap.release()
cv2.destroyAllWindows()
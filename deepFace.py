from deepface import DeepFace
import cv2

# Open the webcam
cap = cv2.VideoCapture(0)

while True:
    # Read a frame from the webcam
    ret, frame = cap.read()

    # If a frame was successfully read
    if ret:
        # Detect emotions in the frame
        result = DeepFace.analyze(frame, actions=['emotion'])

        # Get the dominant emotion
        dominant_emotion = result['dominant_emotion']

        # Print the dominant emotion
        print(dominant_emotion)

        # Display the frame
        cv2.imshow("Emotion Detection", frame)

        # If 'q' is pressed, stop the loop
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

# Release the webcam and destroy all windows
cap.release()
cv2.destroyAllWindows()
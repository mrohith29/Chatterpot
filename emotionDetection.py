# import cv2
# import numpy as np
# from tensorflow import load_model


# model = load_model('expression_model.h5')

# face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# cap = cv2.VideoCapture(0)

# labels = ['Angry', 'Disdust', 'Fear', 'Happy', 'Sad', 'Surprise', 'Neitral']

# while True:

#     _, img = cap.read()

#     gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#     faces = face_cascade.detectMultiScale(img, cv2.COLOR_BGR2GRAY)

#     for (x, y, z, h) in faces:
#         face = gray[y:y+h, x:x+w]
#         face = face / 255.0
#         face = np.expand_dims(face, axis=0)
#         face = np.expand_dims(face, axis=-1)

#         prediction = model.predict(face)
#         emotion = labels[np.argmax(prediction)]

#         cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
#         cv2.putText(img, emotion, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255,0,0), 2)
        
#     cv2.imshow('img', img)

#     if cv2.waitKey(1):
#         break

# cap.release()
# cv2.destroyAllWindows()

# # import cv2
# # import numpy as np
# # from tensorflow.keras.models import load_model

# # model = load_model('expression_model.h5')

# # face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# # cap = cv2.VideoCapture(0)

# # labels = ['Angry', 'Disdust', 'Fear', 'Happy', 'Sad', 'Surprise', 'Neitral']

# # while True:

# #     _, img = cap.read()

# #     gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# #     faces = face_cascade.detectMultiScale(gray, 1.1, 4)

# #     for (x, y, w, h) in faces:
# #         face = gray[y:y+h, x:x+w]


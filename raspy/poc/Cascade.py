import numpy as np
import cv2


faceCascade = cv2.CascadeClassifier('static/haarcascade_frontalface_default.xml')


def imageRead(path):
  return cv2.imread(path)


def imageFromBinary(data):
  img_array = np.asarray(bytearray(data), dtype=np.uint8)
  return cv2.imdecode(img_array, cv2.IMREAD_UNCHANGED)


def imageRead2(path):
  with open(path, 'rb') as f:
    return imageFromBinary(f.read())


imageColor = imageRead2('messi5.jpg')
imageGray = cv2.cvtColor(imageColor, cv2.COLOR_BGR2GRAY)


facesLimits = faceCascade.detectMultiScale(imageGray, 1.3, 5)
faces = [imageColor[y:y+h, x:x+w] for (x,y,w,h) in facesLimits]
idx = 0
for sub_face in faces:
  idx += 1
  faceFileName = "face_" + str(idx) + ".jpg"
  cv2.imwrite(faceFileName, sub_face)

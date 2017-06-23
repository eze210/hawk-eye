import numpy as np
import cv2


class CV2Wrapper(object):
	"""OpenCV 2 Wrapper"""

	def __init__(self):
		self.faceCascade = cv2.CascadeClassifier('static/haarcascade_frontalface_default.xml')


	def imageRead(self, path):
	  return cv2.imread(path)


	def imageFromBinary(self, data):
	  imgArray = np.asarray(bytearray(data), dtype=np.uint8)
	  return cv2.imdecode(imgArray, cv2.IMREAD_UNCHANGED)


	# for documentation only
	def imageReadUsingOpen(self, path):
	  with open(path, 'rb') as f:
	    return self.imageFromBinary(f.read())


	def toGrayScale(self, imageColor):
		return cv2.cvtColor(imageColor, cv2.COLOR_BGR2GRAY)
	

	def detectFacesLimits(self, imageGray):
		return self.faceCascade.detectMultiScale(imageGray, 1.3, 5)


	def detectFaces(self, imageColor):
		imageGray = self.toGrayScale(imageColor)
		facesLimits = self.detectFacesLimits(imageGray)
		return [imageColor[y:y+h, x:x+w] for (x,y,w,h) in facesLimits]


	def imageToBinary(self, image):
		return cv2.imencode('.jpg', image)[1].tostring()


	def imagesCompare(image1, image2):
		return True

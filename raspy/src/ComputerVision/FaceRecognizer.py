import CV2Wrapper
import numpy as np

class FaceRecognizer(object):
	"""FaceRecognizer"""

	def __init__(self):
		self.cv = CV2Wrapper.CV2Wrapper()
		self.faceRecognizer = self.cv.createFaceRecognizer()


	def train(self, images, labels):
		return self.faceRecognizer.train(images, np.array(labels))


	def update(self, images, labels):
		return self.faceRecognizer.update(images, np.array(labels))


	def predict(self, image):
		return self.faceRecognizer.predict(image)

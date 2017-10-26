import ComputerVision.CV2Wrapper


class FaceDetector(object):
	"""FaceDetector"""

	def __init__(self):
		self.cv = CV2Wrapper.CV2Wrapper()


	def detectFromImage(self, image):
		return self.cv.detectFaces(image)


	def detectFromPath(self, imagePath):
		image = self.cv.imageRead(imagePath)
		return self.detectFromImage(image)


	def detectFromBinary(self, imageBin):
		image = self.cv.imageFromBinary(imageBin)
		return self.detectFromImage(image)

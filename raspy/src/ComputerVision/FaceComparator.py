from ComputerVision.CV2Wrapper import CV2Wrapper


class FaceComparator(object):
	"""FaceComparator"""

	def __init__(self):
		self.cv = CV2Wrapper()


	def facesCompare(self, image1, image2):
		return self.cv.imagesCompare(image1, image2)

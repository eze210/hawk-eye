import CV2Wrapper

from cv2 import imwrite

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


if __name__ == '__main__':
	fd = FaceDetector()
	faces = fd.detectFromPath('poc/messi5.jpg')

	idx = 0
	for sub_face in faces:
		idx += 1
		faceFileName = "poc/face_" + str(idx) + ".jpg"
		imwrite(faceFileName, sub_face)

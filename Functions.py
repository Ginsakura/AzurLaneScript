import cv2
import ADBFunctions as adbf

def getImage():
	# opencv读取内存图片
	cv.imdecode(numpy.asarray(adbf.screencap(), dtype=numpy.uint8), cv.IMREAD_COLOR)

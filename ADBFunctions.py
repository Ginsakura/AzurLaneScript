import os
import cv2
import json
import subprocess

class AdbOperation(object):
	threshold = 0.8
	timeout = 1
	"""docstring for AdbOperation"""
	def __init__(self, test_device=False):
		super(AdbOperation, self).__init__()
		self.adbPath = '%s/Adb/adb.exe'%os.getcwd()
		with open('./config.json','r') as self.config:
			self.config = json.load(self.config)
		if test_device:
			AdbCheck()
		
	def screencap():
		byteImage = run('shell screencap -p').replace(b'\r\n', b'\n').replace(b'\r\n', b'\n')
		# 返回字节码
		return bytearray(byteImage)

	# 执行命令
	def run(cmdStr: str=''):
		cmds = [self.adbPath,'-s',self.config["DeviceHostPort"]]+cmdStr.split(' ')
		proc = subprocess.Popen(
			cmds,
			stdin=subprocess.PIPE,
			stdout=subprocess.PIPE,
			stderr=subprocess.PIPE,
		)
		stdout, stderr = proc.communicate()
		# returncode 代表执行cmd命令报错
		if proc.returncode > 0:
			raise Exception(proc.returncode, stderr)
		return (stdout, stderr)

class AdbCheck(object):
	"""docstring for AdbCheck"""
	adb = AdbOperation()

	def __init__(self):
		super(AdbCheck, self).__init__()
		self.AdbCheck()
		self.LinkCheck()

	def AdbCheck(self):
		print("ADB Path >>>> %s"%adb.adbPath,end='\t')
		try:
			subprocess.Popen(
				[adb.adbPath], 
				stdout=subprocess.PIPE, 
				stderr=subprocess.PIPE
				)
		except OSError:
			print('×\tPath Error')
			exit(1)
		else:
			print('√\tPass')

	def LinkCheck(self):
		print("Check device link status >>>> %s"%adb.config["DeviceHostPort"],end='\t')
		stdout,stderr = adb.run("devices")
		deviceList = stdout.decode().replace("\t","\r\n").split("\r\n")
		if adb.config["DeviceHostPort"] in deciceList:
			print('√\tPass')
		else:
			print('×\tDevice does not exist')
		print(stdout.decode())
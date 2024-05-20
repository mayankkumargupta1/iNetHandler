from speedtest import Speedtest

class Upload(Speedtest):
	
	def get(self):
		try:
			a = self.upload()
			return a / 1000000
		except:
			return 0
if __name__ == '__main__':
	a = Upload()
	print(a.get())
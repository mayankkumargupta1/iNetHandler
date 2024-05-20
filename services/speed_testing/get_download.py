from speedtest import Speedtest

class Download(Speedtest):
	def get(self):
		try:
			a = self.download()
			return a / 1000000
		except:
			return 0
if __name__ == "__main__":
	test = Download()
	print(test.get())
	
import subprocess

class Disconnect:
	def unestablish_connection(self):
		command = "netsh wlan disconnect"
		output = subprocess.check_output(command, shell = True)
		output_str = output.decode('utf-8');
		if output_str.find('successfully') != -1:
			return True
		else:
			return False


if __name__ == "__main__":
	a= Disconnect()
	a.unestablish_connction()
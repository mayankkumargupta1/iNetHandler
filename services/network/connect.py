import subprocess
import os

class Connect:
	def wifi_status(self):
		command = "netsh wlan show interfaces"
		output = subprocess.check_output(command, shell=True)
		output_str = output.decode("utf-8")
		if output_str.find('Software Off') != -1:
			return False
		else:
			return True

	def establish_connection(self, name: str, SSID: str) -> bool:
		try:
			command = "netsh wlan connect name=\""+name+"\" ssid=\""+SSID+"\" interface=Wi-Fi"
			output = subprocess.check_output(command, shell=True)
			str_output = output.decode("utf-8")
			if str_output.find("successfully") == -1:
				return False
			else:
				return True
		except:
			return False
	

if __name__ == "__main__":
	a = Connect()
	print(a.establish_connection("moto g51 5G_5897","moto g51 5G_5897"))
	# print(a.wifi_status())
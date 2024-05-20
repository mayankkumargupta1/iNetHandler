import subprocess
import re


class checkAvailable:
	def check(self):
		command = "netsh wlan show networks"

		matches = re.findall( r'SSID \d+ : (.+)' , subprocess.check_output(command, shell = True).decode('utf-8') )
		matches = list(matches)
		for i in range(len(matches)):
			matches[i] = matches[i][:len(matches[i])-1]
		return tuple(matches)
	
	def network_history(self):
		command = "netsh wlan show profiles"
		out = subprocess.check_output(command, shell = True).decode('utf-8')
		pattern = r"All User Profile\s*:\s*(.+)"
		matches = list(re.findall(pattern, out))
		for i in range(len(matches)):
			matches[i] = matches[i][:len(matches[i])-1]
		return tuple(matches)	

if __name__ == "__main__" :
	a = checkAvailable()

	print(a.network_history());
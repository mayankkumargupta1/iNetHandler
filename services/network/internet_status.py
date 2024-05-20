import urllib3

class internet:
	def connection_status(self):
		try:
			http = urllib3.PoolManager(timeout=3.0)
			r = http.request('GET', 'google.com', preload_content=False)
			code = r.status
			r.release_conn()
			if code == 200:
			    return True
			else:
			    return False
		except:
			return False

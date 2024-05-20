import requests
import time


class Download():
	def measure_download_speed(self,url):
	    try:
	        start_time = time.time()
	        response = requests.get(url, stream=True)
	        response.raise_for_status()
	        response.content  # Force download to complete
	        end_time = time.time()
	        bytes_downloaded = len(response.content)
	        download_speed_bps = bytes_downloaded / (end_time - start_time)
	        return download_speed_bps
	    except requests.RequestException as e:
	        print(f"Error during download test: {e}")
	        return None

	def main(self):
	    download_url = "https://speed.cloudflare.com/__down?bytes=100000000"  # 100 MB
	    
	    print("Measuring download speed...")
	    download_speed_bps = self.measure_download_speed(download_url)
	    if download_speed_bps:
	        download_speed_mbps = download_speed_bps / 1_000_000
	        print(f"Download speed: {download_speed_mbps:.2f} Mbps")
	        return(download_speed_mbps)
	    else:
	        print("Failed to measure download speed.")
	        return(0)

	def get(self):
		try:
			return self.main()
		except:
			return 0

if __name__ == "__main__":
	test = Download()
	print(test.get())
	

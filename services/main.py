from services.network import check_available,connect,disconnect,internet_status
from services.speed_testing import get_download,get_upload
import time

class Odin():
    def refresh(self) -> bool:
        if connect.Connect().wifi_status():    
            disconnect.Disconnect().unestablish_connection()
            current = set(check_available.checkAvailable().check())
            past = set(check_available.checkAvailable().network_history())
            available = current.intersection(past)
            
            print(available)
            fastest = ""
            speed = 0
            for i in available:
                print(i)
                if connect.Connect().establish_connection(i,i):
                    
                    for j in range(10):
                        time.sleep(2)
                        if check_available.checkAvailable().check()[0] == i:
                            break
                    print("checking speed")
                    try:
                        net_speed = get_download.Download().get()
                    except:
                        net_speed = 0

                    print(net_speed)
                    if net_speed > speed:
                        fastest = i
                        speed = net_speed
                    disconnect.Disconnect().unestablish_connection()

            print("fastest Internet is", fastest)
            connect.Connect().establish_connection(fastest,fastest)

        else:
            print("Turn on wifi")

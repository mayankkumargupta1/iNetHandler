import customtkinter
import threading
from services.main import Odin
from services.network import internet_status
import pystray
from pystray import MenuItem as item
from PIL import Image
import time
import os
import sys

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


class Internet_handler(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("iNetHandler")
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        window_width = 300
        window_height = 150
        # Calculate x and y coordinates for the center
        x_position = (screen_width // 2) - (window_width // 2)
        y_position = (screen_height // 2) - (window_height // 2)
        # Set the window geometry to the calculated position
        self.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")



        self.after(201, lambda :self.iconbitmap(resource_path('icon.ico'))) 
        

        self.resizable(False, False)
        self.manual_refresh = False
        self.handler = Odin()
        self.application_running = True
        self.refresh_btn_color = "#980347"
        self.configure(fg_color = "black", bg_color = "black")
        self.refresh_button = customtkinter.CTkButton(self, text="Refresh",corner_radius = 3, command=self.refresh_button_action,text_color_disabled = "#E3B505", fg_color=self.refresh_btn_color, hover_color = "#FF27A5", font=("Verdana", 16))
        self.refresh_button.pack(expand = True)
        
        self.protocol("WM_DELETE_WINDOW", self.close_button_action)

        self.Listen = threading.Thread(target = self.listen).start()

        self.withdraw()
        self.create_tray_icon()
    
    def listen(self):
    	while self.application_running:
    		time.sleep(10)
    		if internet_status.internet().connection_status() == False and self.manual_refresh == False:
    			self.refresh_button.configure(state = "disabled", text = "Refreshing")
    			self.handler.refresh()
    			self.refresh_button.configure(state = "normal", text = "Refresh")
    		

    def refresh(self):
    	self.manual_refresh = True
    	self.refresh_button.configure(state = "disabled", text = "Refreshing")
    	self.handler.refresh()
    	self.refresh_button.configure(state = "normal", text = "Refresh")
    	self.manual_refresh = False


    def refresh_button_action(self):
        threading.Thread(target=self.refresh).start()

    def close_button_action(self):
    	self.withdraw()

    def create_tray_icon(self):
        # Load your custom icon
        image = Image.open(resource_path("icon.ico"))
        menu = (item('Show', self.show_window), item('Exit', self.exit_app))
        self.tray_icon = pystray.Icon("name", image, "iNetHandler", menu)

        # Run the icon in a separate thread to avoid blocking the main thread
        threading.Thread(target=self.tray_icon.run, daemon=True).start()

    def show_window(self):
        # Show the main window and hide the tray icon
        self.deiconify()
        

    def exit_app(self):
        # Exit the application
        self.application_running = False
        self.tray_icon.stop()
        self.quit()


if __name__ == "__main__":
    app = Internet_handler()
    app.mainloop()

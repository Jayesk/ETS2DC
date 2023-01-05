import os, os.path
import tkinter as tk
import tkinter.messagebox
import tkinter.simpledialog
import pyautogui
import time
from PIL import Image



# Set Screenshot Area
f = open("config.txt", "r")
ftext = str(f.readlines())
for c in "{}'[]":
    ftext = ftext.replace(c, "")
print(ftext)
coordinatesforscreenshot = ftext
f.close()
f = open("config.txt", "r")
f.close()
print(coordinatesforscreenshot)

class App:
    def __init__(self):
        # Create the main window
        self.root = tk.Tk()
        self.root.title("Jayesk's Screenshotter")
        self.root.geometry("350x200")  # Set the size of the window
        self.root.iconbitmap("icon.ico")

        # Create the menubar
        self.menubar = tk.Menu(self.root)

        # Create the "Setup" menu
        self.settings_menu = tk.Menu(self.menubar, tearoff=0)
        self.settings_menu.add_command(label="Coords Finder...", command=self.coordfinder)
        self.menubar.add_cascade(label="Setup", menu=self.settings_menu)

        # Create the "Presets" menu
        self.settings_menu = tk.Menu(self.menubar, tearoff=0)
        self.settings_menu.add_command(label="Presets...", command=self.screenshot_area_window)
        self.menubar.add_cascade(label="Presets", menu=self.settings_menu)

        # Create the "Settings" menu
        self.settings_menu = tk.Menu(self.menubar, tearoff=0)
        self.settings_menu.add_command(label="Screenshot Area...", command=self.screenshot_area_alt_window)
        self.settings_menu.add_command(label="Screenshot Frequency...", command=self.change_screenshot_interval)
        self.menubar.add_cascade(label="Settings", menu=self.settings_menu)

        # Create the "Troubleshooting" menu
        self.settings_menu = tk.Menu(self.menubar, tearoff=0)
        self.settings_menu.add_command(label="Screenshot Counter...", command=self.screenshotcountermenu)
        self.settings_menu.add_command(label="ETS2 Check...", command=self.ets2checkmenu)
        self.menubar.add_cascade(label="Troubleshooting", menu=self.settings_menu)

        # Add the menubar to the window
        self.root.config(menu=self.menubar)

        # Create a "Start Recording" button
        self.start_button = tk.Button(self.root, text="Start Recording", command=self.start_recording)
        self.start_button.pack()

        # Create a "Stop Recording" button
        self.stop_button = tk.Button(self.root, text="Stop Recording", command=self.stop_recording)
        self.stop_button.pack()

        # Set the recording flag to False
        self.recording = False

        # Set the screenshot interval to 0.5 seconds
        self.screenshot_interval = 0.5

        # Default counter value:
        DIR = 'captured'
        if len([name for name in os.listdir(DIR) if os.path.isfile(os.path.join(DIR, name))]) >= 1:
            self.counter = len([name for name in os.listdir(DIR) if os.path.isfile(os.path.join(DIR, name))])
        
        else:
            self.counter = 0

        # Create a counter label
        self.counter_label = tk.Label(self.root, text=f"Screenshots Taken: {self.counter}")
        self.counter_label.pack()

        # Create a label to display the screenshot
        self.label = tk.Label(self.root)
        self.label.pack()

    def coordfinder(self):
        self.coordfinder = tk.Toplevel(self.root)
        self.coordfinder.geometry("160x84")
        self.coordfinder.iconbitmap("icon.ico")
        self.set_button = tk.Button(self.coordfinder, text="Get 1st Set Of Coords...", command=self.coordset)
        self.set_button.pack()
        self.set_button = tk.Button(self.coordfinder, text="Get 2nd Set Of Coords...", command=self.coordset)
        self.set_button.pack()
        self.set_button = tk.Button(self.coordfinder, text="Clear Coords...", command=self.coordclear)
        self.set_button.pack()

    def coordset(self):

        coordset = tk.Toplevel(self.root)

        f = open("config.txt", "a+")
        fchar = f.read()
        screen_width, screen_height = pyautogui.size()

        time.sleep(5)
        x, y = pyautogui.position()
        y = screen_height - y

        text = tk.Text(coordset, height=2, width=90)
        text.pack()
        text.insert(tk.END, f"x: {x}, y: {y}")

        f.write(f"{x}, {y}, ")
        f.close()

    def coordclear(self):
        f = open("config.txt", "w+")
        f.truncate(0)
        f.close()
        tk.messagebox.showinfo("Coords Cleared.", "Coords have been cleared, you can now enter new coords.")

    def screenshotcountermenu(self):
        self.screenshotcountermenu = tk.Toplevel(self.root)
        self.screenshotcountermenu.geometry("250x84")
        self.screenshotcountermenu.iconbitmap("icon.ico")

        # Create the Screenshot count label
        self.scrnshotctr = tk.Label(self.screenshotcountermenu, text="Enter Screenshot Count:")
        self.scrnshotctr.pack()

        # Create the Screenshot count entry
        self.scrnshotctr = tk.Entry(self.screenshotcountermenu)
        self.scrnshotctr.pack()

        # Create the "Save" button
        self.set_button = tk.Button(self.screenshotcountermenu, text="Save", command=self.screenshotcountvalue)
        self.set_button.pack()

    def screenshotcountvalue(self):
        self.counter = int(self.scrnshotctr.get())
        print(self.counter)

    def screenshot_area_alt_window(self):
        # Create the screenshot area window
        self.screenshot_area_alt_window = tk.Toplevel(self.root)
        self.screenshot_area_alt_window.title("Screenshot Area")
        self.screenshot_area_alt_window.geometry("300x300")
        self.screenshot_area_alt_window.iconbitmap("icon.ico")

        # Create the x1 label
        self.x1_label = tk.Label(self.screenshot_area_alt_window, text="\nSet 1\n\nCoord 1")
        self.x1_label.pack()

        # Create the x1 entry
        self.x1_entry = tk.Entry(self.screenshot_area_alt_window)
        self.x1_entry.pack()

        # Create the y1 label
        self.y1_label = tk.Label(self.screenshot_area_alt_window, text="Coord 2")
        self.y1_label.pack()

        # Create the y1 entry
        self.y1_entry = tk.Entry(self.screenshot_area_alt_window)
        self.y1_entry.pack()

        # Create the x2 label
        self.x2_label = tk.Label(self.screenshot_area_alt_window, text="\nSet 2\n\n Coord 1:")
        self.x2_label.pack()

        # Create the x2 entry
        self.x2_entry = tk.Entry(self.screenshot_area_alt_window)
        self.x2_entry.pack()

        # Create the y2 label
        self.y2_label = tk.Label(self.screenshot_area_alt_window, text="Coord 2")
        self.y2_label.pack()

        # Create the y2 entry
        self.y2_entry = tk.Entry(self.screenshot_area_alt_window)
        self.y2_entry.pack()

        # Create the "Set" button
        self.set_button = tk.Button(self.screenshot_area_alt_window, text="Set", command=self.set_screenshot_area)
        self.set_button.pack()

    def set_screenshot_area(self):
        # Get the values from the entries
        x1 = self.x1_entry.get()
        y1 = self.y1_entry.get()
        x2 = self.x2_entry.get()
        y2 = self.y2_entry.get()

        f = open("config.txt", "w+")
        f.write(str(x1))
        f.write(", ")
        f.write(str(y1))
        f.write(", ")
        f.write(str(x2))
        f.write(", ")
        f.write(str(y2))
        f.write(", ")
        f.close()

        # Check if all values are integers
        if not all(value.isdigit() for value in [x1, y1, x2, y2]):
            # Display an error message
            tk.messagebox.showerror("Error", "Invalid values. Please enter integers.")
            return

    def screenshot_area_window(self):
        # Create the screenshot area window
        self.screenshot_area_window = tk.Toplevel(self.root)
        self.screenshot_area_window.title("Screenshot Area")
        self.screenshot_area_window.geometry("200x80")  # Set the size of the window
        self.screenshot_area_window.iconbitmap("icon.ico")

        # Create the "Scania S" button
        self.set_button = tk.Button(self.screenshot_area_window, text="Scania S", command=self.scania_s_preset)
        self.set_button.pack()

        # Create the "Volvo FH16" button
        self.set_button = tk.Button(self.screenshot_area_window, text="Volvo FH16", command=self.volvo_fh16_preset)
        self.set_button.pack()

        # Create the "DAF 2021" button
        self.set_button = tk.Button(self.screenshot_area_window, text="DAF 2021", command=self.daf_2021_preset)
        self.set_button.pack()

    def scania_s_preset(self):
        # Destroy the screenshot area window
        self.screenshot_area_window.destroy()
        tk.messagebox.showinfo("Error", "Scania S does not have a preset.")
        self.screenshot_area = (0, 0, 100, 100)

    def volvo_fh16_preset(self):
        # Destroy the screenshot area window
        self.screenshot_area_window.destroy()
        tk.messagebox.showerror("Error", "Volvo FH16 does not have a preset.")
        self.screenshot_area = (x1, y1, x2, y2)

        # Destroy the screenshot area window
        self.screenshot_area_window.destroy()

    def daf_2021_preset(self):
        # Destroy the screenshot area window
        self.screenshot_area_window.destroy()
        tk.messagebox.showerror("Error", "DAF 2021 does not have a preset.")
        self.screenshot_area = (x1, y1, x2, y2)

        # Destroy the screenshot area window
        self.screenshot_area_window.destroy()

    def ets2checkmenu(self):
        # Create the ets2check window
        self.ets2checkmenu = tk.Toplevel(self.root)
        self.ets2checkmenu.title("Screenshot Area")
        self.ets2checkmenu.geometry("160x26")  # Set the size of the window
        self.ets2checkmenu.iconbitmap("icon.ico")

        # Create the "ETS2 Bypass" button
        self.set_button = tk.Button(self.ets2checkmenu, text="ETS2 Check Bypass", command=self.ets2checkbypass)
        self.set_button.pack()

    def ets2checkbypass(self):
        self.ets2checkmenu.destroy()
        self.ets2checkbypass = tk.Toplevel(self.root)
        self.ets2checkbypass.title("Euro Truck Simulator 2")
        self.ets2checkbypass.geometry("400x36")
        self.ets2checkbypass.iconbitmap("icon.ico")
        T = tk.Text(self.ets2checkbypass, height=2, width=90)
        T.pack()
        T.insert(tk.END, "This is a dummy window for testing purposes")  

    def start_recording(self):
        # Try to find the "Euro Truck Simulator 2" window
        try:
            window = pyautogui.getWindowsWithTitle("Euro Truck Simulator 2")[0]
        except:
            # If the window is not found, show an error message
            tk.messagebox.showerror("Error", "Euro Truck Simulator 2 window not found")
            return

        # Set the recording flag to True
        self.recording = True

        # Start the screenshot loop
        self.root.after(int(self.screenshot_interval * 1000), self.screenshot_loop)

    def stop_recording(self):
        # Set the recording flag to False
        self.recording = False


    def screenshot_loop(self):
        # Check if the recording flag is set
        if self.recording:
            # Increment the screenshot counter
            self.counter += 1
            print(self.counter)

            # Take screenshot of the defined area
            image = pyautogui.screenshot(region=(668, 313, 700, 400))

            # Save the image to the "captured" folder
            image.save(f"captured/{self.counter}.png")

            # Convert the image to a PhotoImage object
            image = tk.PhotoImage(file=f"captured/{self.counter}.png")

            # Update the label's image
            self.label.config(image=image)
            self.label.image = image
            # Update the counter label
            self.counter_label.config(text=f"Screenshots Taken: {self.counter}")

            # Schedule the next screenshot
            self.root.after(int(self.screenshot_interval * 500), self.screenshot_loop)

    def change_screenshot_interval(self):
        interval = tk.simpledialog.askfloat("Screenshot Interval", "Enter the new screenshot interval (in seconds):", minvalue=0.1, maxvalue=10)

        # Check if the user entered a valid interval
        if interval is not None:
            # Set the new interval
            self.screenshot_interval = interval

# Create the app and start the main loop
app = App()
app.root.mainloop()
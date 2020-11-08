# Importing the library
from tkinter import *


class MainGUI:
    def __init__(self):
        self.root = Tk()
        self.root.title("Phone Price Predictor")
        pass

    #! Building the Graphical User Interface
    def buildGUI(self):
        canvas = Canvas(self.root, height=800, width=600, bg='#4287f5')
        canvas.pack()
        # Label
        main_label = Label(canvas, text="Phone Price Predictor", bg='#4287f5')
        main_label.place(relx=0.2, rely=0, relwidth=0.6, relheight=0.1)
        # All The Text Fields
        # Left Side Labels
        battery_label = Label(
            canvas, text="Battery Capacity (mAh)", bg="#4287f5", font=("Courier", 15))
        battery_label.place(relx=0, rely=0.1, relwidth=0.5, relheight=0.05)
        bt_label = Label(
            canvas, text="Has Bluetooth? (1 or 0)", bg="#4287f5", font=("Courier", 15))
        bt_label.place(relx=0, rely=0.15, relwidth=0.5, relheight=0.05)
        clk_spd_label = Label(
            canvas, text="Clock Speed (GHz)", bg="#4287f5", font=("Courier", 15))
        clk_spd_label.place(relx=0, rely=0.2, relwidth=0.5, relheight=0.05)
        dual_sim_label = Label(
            canvas, text="Has Dual Sim? (1 or 0)", bg="#4287f5", font=("Courier", 15))
        dual_sim_label.place(relx=0, rely=0.25, relwidth=0.5, relheight=0.05)
        selfie_cam_label = Label(
            canvas, text="Selfie Cam Res (mp)", bg="#4287f5", font=("Courier", 15))
        selfie_cam_label.place(relx=0, rely=0.25, relwidth=0.5, relheight=0.05)
        has_4g_label = Label(
            canvas, text="Has 4G? (1 or 0)", bg="#4287f5", font=("Courier", 15))
        has_4g_label.place(relx=0, rely=0.3, relwidth=0.5, relheight=0.05)
        memory_label = Label(
            canvas, text="Memory (GB)", bg="#4287f5", font=("Courier", 15))
        memory_label.place(relx=0, rely=0.35, relwidth=0.5, relheight=0.05)
        depth_label = Label(
            canvas, text="Depth (cm)", bg="#4287f5", font=("Courier", 15))
        depth_label.place(relx=0, rely=0.4, relwidth=0.5, relheight=0.05)
        # Right Side Txt Fields
        battery_entry = Entry(canvas, font=("Courier", 15))
        battery_entry.place(relx=0.5, rely=0.1, relwidth=0.5, relheight=0.05)
        bt_entry = Entry(
            canvas, font=("Courier", 15))
        bt_entry.place(relx=0.5, rely=0.15, relwidth=0.5, relheight=0.05)
        # Buttons
        execute_button = Button(canvas, text="Execute")
        execute_button.place(relx=0.3, rely=0.9, relwidth=0.4, relheight=0.095)
        pass

    #! Showing the Graphical User Interface
    def showGUI(self):
        self.root.mainloop()
        pass


# Testing
GUI = MainGUI()
GUI.buildGUI()
GUI.showGUI()

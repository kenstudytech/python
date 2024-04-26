import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk # Require this module to support the image resizing

class MyApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Flatpak CheckInstaller")
        #self.root.geometry("1600x900")

        # Frame 1
        self.frame1 = tk.Frame(root, bg="red", height=100)
        self.frame1.pack(fill=tk.X)

        # Load PNG icons and resize them
        try:
            self.open_icon = Image.open("open.png").resize((40, 40))
            self.open_icon = ImageTk.PhotoImage(self.open_icon)

            self.save_icon = Image.open("save.png").resize((40, 40))
            self.save_icon = ImageTk.PhotoImage(self.save_icon)

            self.distro_icon = Image.open("distro.png").resize((40, 40))
            self.distro_icon = ImageTk.PhotoImage(self.distro_icon)

            self.about_icon = Image.open("about.png").resize((40, 40))
            self.about_icon = ImageTk.PhotoImage(self.about_icon)

            self.exit_icon = Image.open("exit.png").resize((40, 40))
            self.exit_icon = ImageTk.PhotoImage(self.exit_icon)
        except tk.TclError as e:
            print("Error loading PNG files:", e)


        # Create buttons with PNG icons
        open_button = tk.Button(self.frame1, image=self.open_icon, text="Open", compound=tk.LEFT, width=100, height=50)
        save_button = tk.Button(self.frame1, image=self.save_icon, text="Save", compound=tk.LEFT, width=100, height=50)
        distro_button = tk.Button(self.frame1, image=self.distro_icon, text="Distro", compound=tk.LEFT, width=100, height=50, command=self.show_distro)
        about_button = tk.Button(self.frame1, image=self.about_icon, text="About", compound=tk.LEFT, width=100, height=50, command=self.show_about)
        exit_button = tk.Button(self.frame1, image=self.exit_icon, text="Exit", compound=tk.LEFT, width=100, height=50, command=root.quit)


        # Create a label
        software_label = tk.Label(self.frame1, text="Flatpak CheckInstaller", font=("Arial", 20), bg="red", fg="white")

        # Create a placeholder widget
        placeholder = tk.Frame(self.frame1, bg="red")
        placeholder.grid(row=0, column=3, padx=10, pady=10, sticky="e")  # Align to the right

        # Grid buttons, label, and placeholder
        open_button.grid(row=0, column=0, padx=10, pady=10)
        save_button.grid(row=0, column=1, padx=10, pady=10)
        software_label.grid(row=0, column=2, padx=10, pady=10, columnspan=2, sticky="nsew")  # Center the label
        distro_button.grid(row=0, column=4, padx=10, pady=10)
        about_button.grid(row=0, column=5, padx=10, pady=10)
        exit_button.grid(row=0, column=6, padx=10, pady=10)

        # Configure column to expand
        self.frame1.grid_columnconfigure(3, weight=1)


        # Frame 2
        self.frame2 = tk.Frame(root, bg="black", height=300)
        self.frame2.pack(fill=tk.X)

        # Theme the widgets
        style = ttk.Style()
        style.configure("Bold.TLabelframe.Label", font=("Arial", 10, "bold")) #change the font to the groupbox header
        style.configure("Bold.TLabelframe", background="gray")


        for i in range(8):
            group_box = ttk.LabelFrame(self.frame2, text=f"Group Box {i+1}", padding=20, style="Bold.TLabelframe")
            group_box.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10, pady=20)
            group_box.configure(width=200)  # Adjust the width as needed
            for j in range(10):
                tk.Checkbutton(group_box, text=f"Checkbox {j+1}", anchor="w", font=("Arial", 10)).pack(side=tk.TOP, anchor="w")

        # Frame 3
        self.frame3 = tk.Frame(root, bg="green", height=300)
        self.frame3.pack(fill=tk.X)

        for i in range(8):
            group_box = ttk.LabelFrame(self.frame3, text=f"Group Box {i+1}", padding=20, style="Bold.TLabelframe")
            group_box.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10, pady=20)
            group_box.configure(width=200)  # Adjust the width as needed
            for j in range(10):
                tk.Checkbutton(group_box, text=f"Checkbox {j+1}", anchor="w", font=("Arial", 10)).pack(side=tk.TOP, anchor="w")

        # Frame 4
        self.frame4 = tk.Frame(root, bg="yellow", height=200)
        self.frame4.pack(fill=tk.X)

        # Splitting frame4 into 3 sections
        scrollbar1 = tk.Scrollbar(self.frame4, orient=tk.VERTICAL, width=13)
        scrollbar2 = tk.Scrollbar(self.frame4, orient=tk.VERTICAL, width=13)

        listbox1 = tk.Listbox(self.frame4, yscrollcommand=scrollbar1.set, width=20, height=10, selectmode=tk.MULTIPLE)
        scrollbar1.config(command=listbox1.yview)

        listbox2 = tk.Listbox(self.frame4, yscrollcommand=scrollbar2.set, width=20, height=10, selectmode=tk.MULTIPLE)
        scrollbar2.config(command=listbox2.yview)

        labels_entry_frame = tk.Frame(self.frame4, bg="yellow")

        # Grid listboxes, scrollbars, and labels_entry_frame
        listbox1.grid(row=0, column=0, padx=(10,0), pady=5, sticky=tk.NSEW)
        scrollbar1.grid(row=0, column=1, padx=0, pady=5, sticky=tk.NS)

        listbox2.grid(row=0, column=2, padx=(10,0), pady=5, sticky=tk.NSEW)
        scrollbar2.grid(row=0, column=3, padx=(0,10), pady=5, sticky=tk.NS)

        labels_entry_frame.grid(row=0, column=4, padx=5, pady=5, sticky=tk.NSEW)

        tk.Label(labels_entry_frame, text="Total Software:").grid(row=0, column=0, padx=5, pady=5, sticky=tk.E)
        tk.Label(labels_entry_frame, text="Total Selected:").grid(row=1, column=0, padx=5, pady=5, sticky=tk.E)
        tk.Entry(labels_entry_frame).grid(row=0, column=1, padx=5, pady=5, sticky=tk.W)
        tk.Entry(labels_entry_frame).grid(row=1, column=1, padx=5, pady=5, sticky=tk.W)

        # Add a button below the entry textboxes
        button_frame = tk.Frame(labels_entry_frame)
        button_frame.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

        # Create a larger button
        submit_button = tk.Button(button_frame, text="Installation Commandline", width=30, height=4, command=self.show_commandline)
        submit_button.pack()

        # Configure grid weights for Frame 4
        self.frame4.columnconfigure(0, weight=1)
        self.frame4.columnconfigure(2, weight=1)


        # Routine to centre all dialog boxes
    def center_window(self, window):
        # Get the position of the main GUI window
        main_gui_x = self.root.winfo_rootx()
        main_gui_y = self.root.winfo_rooty()

        # Get the width and height of the main GUI window
        main_gui_width = self.root.winfo_width()
        main_gui_height = self.root.winfo_height()

        # Get the width and height of the screen
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        # Calculate the position to center the window relative to the screen
        x = main_gui_x + (main_gui_width - window.winfo_reqwidth()) // 2
        y = main_gui_y + (main_gui_height - window.winfo_reqheight()) // 2

        # Define the offset distance
        offset_x = 5000  # Adjust as needed
        offset_y = 50  # Adjust as needed

        # Ensure the dialog window is within the screen boundaries
        x = max(min(x, screen_width - window.winfo_reqwidth() - offset_x), offset_x)
        y = max(min(y, screen_height - window.winfo_reqheight() - offset_y), offset_y)

        # Adjust the coordinates to center the dialog box on the screen
        x += offset_x // 2
        y += offset_y // 2

        # Set the window position
        window.geometry("+{}+{}".format(x, y))

    def show_about(self):

        # Disable window decorations for the root window
        self.root.overrideredirect(True)

        about_window = tk.Toplevel(self.root)  # Pass self.root as the parent
        about_window.title("About")
        about_window.geometry("400x300")  # Set the width and height of the About window

        # Make the distro window non-resizable
        about_window.resizable(False, False)

        #Create the widgets
        about_label = tk.Label(about_window, text="Flatpak CheckInstaller\nVersion 1.0")
        about_ok_button = tk.Button(about_window, text="OK", width=8, height=2, command=about_window.destroy)

        #pack the widgets
        about_label.pack(padx=20, pady=20)
        about_ok_button.pack(padx=10, pady=10)

        # Make the window modal and transient
        about_window.grab_set()
        about_window.transient(self.root)

        # Center the window
        self.center_window(about_window)

    def show_distro(self):

        # Disable window decorations for the root window
        self.root.overrideredirect(True)

        distro_window = tk.Toplevel(self.root)  # Pass self.root as the parent
        distro_window.title("Distro")
        distro_window.geometry("600x400")  # Set the width and height of the About window

        # Make the distro window non-resizable
        distro_window.resizable(False, False)

        # Create frames
        distro_frame1 = tk.Frame(distro_window)
        distro_frame2 = tk.Frame(distro_window)
        distro_frame3 = tk.Frame(distro_window)

        # Variable to hold the selected distro
        selected_distro = tk.StringVar()

        # Create the text label in frame 1
        distro_label = tk.Label(distro_frame1, text="Select Distro", font=("Arial", 11, "bold"))

        # Create the radio buttons in frame 2
        distro1_radio = tk.Radiobutton(distro_frame2, text="Distro#1", variable=selected_distro, value="Distro#1")
        distro2_radio = tk.Radiobutton(distro_frame2, text="Distro#2", variable=selected_distro, value="Distro#2")
        distro3_radio = tk.Radiobutton(distro_frame2, text="Distro#3", variable=selected_distro, value="Distro#3")
        distro4_radio = tk.Radiobutton(distro_frame2, text="Distro#4", variable=selected_distro, value="Distro#4")
        distro5_radio = tk.Radiobutton(distro_frame2, text="Distro#5", variable=selected_distro, value="Distro#5")
        distro6_radio = tk.Radiobutton(distro_frame2, text="Distro#6", variable=selected_distro, value="Distro#6")
        distro7_radio = tk.Radiobutton(distro_frame2, text="Distro#7", variable=selected_distro, value="Distro#7")

        # Create the textboxes in frame 2
        distro1_textbox = tk.Text(distro_frame2, height=1, width=60)
        distro2_textbox = tk.Text(distro_frame2, height=1, width=60)
        distro3_textbox = tk.Text(distro_frame2, height=1, width=60)
        distro4_textbox = tk.Text(distro_frame2, height=1, width=60)
        distro5_textbox = tk.Text(distro_frame2, height=1, width=60)
        distro6_textbox = tk.Text(distro_frame2, height=1, width=60)
        distro7_textbox = tk.Text(distro_frame2, height=1, width=60)

        # Create the ok button  in frame 3
        distro_ok_button = tk.Button(distro_frame3, text="OK", width=8, height=2, command=distro_window.destroy)

        # Pack the widget in frame 1
        distro_label.pack(padx=20, pady=(5,0))

        # Pack the radio buttons in frame 2
        distro1_radio.grid(row=0, column=0, padx=(20, 5), pady=10, sticky="w")
        distro1_textbox.grid(row=0, column=1, padx=5, pady=10, sticky="w")

        distro2_radio.grid(row=1, column=0, padx=(20, 5), pady=7, sticky="w")
        distro2_textbox.grid(row=1, column=1, padx=5, pady=7, sticky="w")

        distro3_radio.grid(row=2, column=0, padx=(20, 5), pady=7, sticky="w")
        distro3_textbox.grid(row=2, column=1, padx=5, pady=7, sticky="w")

        distro4_radio.grid(row=3, column=0, padx=(20, 5), pady=7, sticky="w")
        distro4_textbox.grid(row=3, column=1, padx=5, pady=7, sticky="w")

        distro5_radio.grid(row=4, column=0, padx=(20, 5), pady=7, sticky="w")
        distro5_textbox.grid(row=4, column=1, padx=5, pady=7, sticky="w")

        distro6_radio.grid(row=5, column=0, padx=(20, 5), pady=7, sticky="w")
        distro6_textbox.grid(row=5, column=1, padx=5, pady=7, sticky="w")

        distro7_radio.grid(row=6, column=0, padx=(20, 5), pady=7, sticky="w")
        distro7_textbox.grid(row=6, column=1, padx=5, pady=7, sticky="w")

        # Pack the ok button in frame 3
        distro_ok_button.pack(padx=10, pady=(0,10))

        # Pack all frames
        distro_frame1.grid(row=0, column=0, columnspan=2, sticky="w", padx=10, pady=10)
        distro_frame2.grid(row=1, column=0, columnspan=2, sticky="w", padx=10, pady=10)
        distro_frame3.grid(row=2, column=0, columnspan=2, sticky="w", padx=10, pady=10)

        # Make the distro window modal and transient to the root window
        distro_window.grab_set()
        distro_window.transient(self.root)

        # Center the window
        self.center_window(distro_window)



    def show_commandline(self):
        commandline_window = tk.Toplevel(self.root)  # Pass self.root as the parent
        commandline_window.title("Commandline")
        commandline_window.geometry("800x200")  # Set the width and height of the About window

        # Make the distro window non-resizable
        commandline_window.resizable(False, False)

        # Create frames
        commandline_frame1 = tk.Frame(commandline_window)
        commandline_frame2 = tk.Frame(commandline_window)
        commandline_frame3 = tk.Frame(commandline_window)

        # Create the widgets
        commandline_label = tk.Label(commandline_frame1, text="Command line: ")
        commandline_textbox = tk.Text(commandline_frame2, height=5, width=100)
        commandline_copy_button = tk.Button(commandline_frame3, text="Copy", width=8, height=2, command=lambda: self.commandline_copy_command(commandline_textbox))
        commandline_ok_button = tk.Button(commandline_frame3, text="OK", width=8, height=2, command=commandline_window.destroy)

        # Pack the widgets
        commandline_label.pack(side=tk.LEFT, padx=20, pady=(10,5))
        commandline_textbox.pack(side=tk.LEFT, padx=10, pady=(0,10))

        # Place buttons using grid inside frame 3
        commandline_copy_button.grid(row=0, column=0, padx=(10, 5), pady=(10, 40))
        commandline_ok_button.grid(row=0, column=1, padx=(5, 10), pady=(10, 40))

        # Pack frames
        commandline_frame1.pack(fill=tk.X)
        commandline_frame2.pack(fill=tk.BOTH, expand=True)
        commandline_frame3.pack(fill=tk.X)

        # Make the window modal and transient
        commandline_window.grab_set()
        commandline_window.transient(self.root)

        # Center the window
        self.center_window(commandline_window)



    def commandline_copy_command(self, commandline_textbox):
        commandline = commandline_textbox.get("1.0", "end-1c")  # Get text from the textbox
        self.root.clipboard_clear()  # Clear the clipboard
        self.root.clipboard_append(commandline)  # Append the command to the clipboard


if __name__ == "__main__":
    root = tk.Tk()
    root.iconphoto(False, tk.PhotoImage(file='icon.png')) #good way to use png icon file without forcing to use an ico file
    app = MyApp(root)
    root.resizable(False, False)  # Disable resizing in both directions
    root.mainloop()

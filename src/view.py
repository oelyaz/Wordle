import tkinter as tk


class View:
    def __init__(self):
        self.root = tk.Tk()
        self.screen_width = self.root.winfo_screenwidth()
        self.screen_height = self.root.winfo_screenheight()
        self.window_width = 500
        self.window_height= 700

        self.root.title('Wordle')
        # centers the application window on screen
        self.root.geometry(f"{self.window_width}x{self.window_height}+"
                           f"{self.screen_width//2-self.window_width//2}+{self.screen_height//2-self.window_height//2}")
        self.root.resizable(False, False)

        self.frame = tk.Frame(self.root, bg="#282828")

        self.grid_frame = tk.Frame(self.frame, bg="#282828")
        self.entries = []
        for col in range(6):
            entry_row = []
            for row in range(5):
                self.entry = tk.Entry(self.grid_frame, width=2,  justify="center",
                                      font=("Terminal", 30), bg="#1d2021", fg="#ebdbb2")
                self.entry.bind("<Key>", lambda e: "break")  # Blocks keyboard input
                self.entry.bind("<Button-1>", lambda e: "break") # Blocks Mouse clicks
                self.entry.grid(column=col, row=row, ipadx=4, ipady=0, padx=2, pady=12)
                entry_row.append(self.entry)
            self.entries.append(entry_row)
        self.grid_frame.place(relx=0.5, rely=0.6, anchor="center")
        self.entries[0][0].focus_set()
        self.entries[0][0].unbind("<Key>")  # Allow keyboard input for this entry

        self.label = tk.Label(self.frame, bg="#282828", fg="#d3869b", text="W6rdle", font=("Terminal", 70))
        self.label.place(relx=0.5, rely=0.15, anchor="center")

        self.frame.pack(fill="both", expand=True)

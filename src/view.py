import tkinter as tk

from src.word_list import WordList


class View:
    def __init__(self):
        self.root = tk.Tk()
        self.screen_width = self.root.winfo_screenwidth()
        self.screen_height = self.root.winfo_screenheight()
        self.window_width = 500
        self.window_height = 700

        self.root.title('Wordle')
        # centers the application window on screen
        self.root.geometry(f"{self.window_width}x{self.window_height}+"
                           f"{self.screen_width // 2 - self.window_width // 2}+{self.screen_height // 2 - self.window_height // 2}")
        self.root.resizable(False, False)

        self.frame = tk.Frame(self.root, bg="#282828")

        self.grid_frame = tk.Frame(self.frame, bg="#282828")
        self.cursor_pos = [0, 0]
        self.entries = []
        for col in range(6):
            entry_row = []
            for row in range(6):
                self.entry = tk.Entry(self.grid_frame, width=2, justify="center",
                                      font=("Terminal", 30), bg="#1d2021", fg="#ebdbb2")
                self.entry.bind("<KeyPress>", lambda e: "break")  # Blocks keyboard input
                self.entry.bind("<Button-1>", lambda e: "break")  # Blocks Mouse clicks
                self.entry.grid(column=col, row=row, ipadx=4, ipady=0, padx=2, pady=12)
                entry_row.append(self.entry)
            self.entries.append(entry_row)
        self.grid_frame.place(relx=0.5, rely=0.6, anchor="center")
        self.entries[0][0].focus_set()
        self.entries[0][0].bind("<KeyPress>", self.focus_next)  # Allow keyboard input for this entry

        self.label = tk.Label(self.frame, bg="#282828", fg="#d3869b", text="W6rdle", font=("Terminal", 70))
        self.label.place(relx=0.5, rely=0.15, anchor="center")

        self.wordlist = WordList()
        self.frame.pack(fill="both", expand=True)

    def game_loop(self):
        self.root.mainloop()

    def focus_next(self, event):
        entry = self.entries[self.cursor_pos[0]][self.cursor_pos[1]]
        if event.keysym == "BackSpace":
            direction = -1
            entry.delete(0, tk.END)
        elif event.char.isalpha():
            direction = 1
            entry.delete(0, tk.END)
            entry.insert(0, event.char.capitalize())
        elif event.keysym == "Return":
            if self.cursor_pos[0] == 5:
                self.next_row()
            return "break"
        else:
            return "break"

        # deactivate current letter
        entry.bind("<KeyPress>", lambda e: "break") # Blocks keyboard input
        entry.bind("<Button-1>", lambda e: "break")  # Blocks Mouse clicks

        if 6 > self.cursor_pos[0] + direction >= 0:
            self.cursor_pos[0] += direction
            entry = self.entries[self.cursor_pos[0]][self.cursor_pos[1]]

        # activate new letter
        entry.focus_set()
        entry.bind("<KeyPress>", self.focus_next)  # Allow keyboard input for this entry

        return "break"

    def next_row(self):
        trial_word = ''
        for entry in self.entries[self.cursor_pos[1]]:
            trial_word += entry.get()
        if trial_word in self.wordlist.get_dictionary():
            print('öalksdfjölgalg')
            return
        else:
            self.entries[0][self.cursor_pos[0]].configure(bg='#fe8019')
            for i in range(5):
                if trial_word[i] in self.wordlist.get_solution():
                    self.entries[self.cursor_pos[1]][i].configure(bg='#fe8019')
                if trial_word[i] == self.wordlist.get_solution()[i]:
                    self.entries[self.cursor_pos[1]][i].configure(bg='#98971a')

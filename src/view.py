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
            entry.delete(0, "end")
            self.entries[self.cursor_pos[0]-1][self.cursor_pos[1]].delete(0, tk.END)
        elif event.char.isalpha():
            direction = 1
            entry.delete(0, tk.END)
            entry.insert(0, event.char.upper())
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
        for i in range(6):
            trial_word += self.entries[i][self.cursor_pos[1]].get()
        if trial_word not in self.wordlist.get_dictionary():
            return
        else:
            win_condition = 0
            for i in range(6):
                if trial_word[i] in self.wordlist.get_solution():
                    self.entries[i][self.cursor_pos[1]].configure(bg='#fe8019')
                    if trial_word[i] == self.wordlist.get_solution()[i]:
                        win_condition += 1
                        self.entries[i][self.cursor_pos[1]].configure(bg='#98971a')

        entry = self.entries[self.cursor_pos[0]][self.cursor_pos[1]]
        entry.bind("<KeyPress>", lambda e: "break")  # Blocks keyboard input
        entry.bind("<Button-1>", lambda e: "break")  # Blocks Mouse clicks
        if self.cursor_pos[1]+1 < 6:
            self.cursor_pos[1] += 1
            self.cursor_pos[0] = 0
            entry = self.entries[self.cursor_pos[0]][self.cursor_pos[1]]
            entry.focus_set()
            entry.bind("<KeyPress>", self.focus_next)  # Allow keyboard input for this entry
        else:
            for widget in self.grid_frame.winfo_children():
                widget.destroy()  # Remove all child widgets
            label = tk.Label(self.grid_frame, bg="#282828", text="VERLOREN!", font=("Terminal", 50), fg='#98971a')
            label.place(relx=0.5, rely=0.2, anchor="center")
            label_loes = tk.Label(self.grid_frame, bg="#282828", text=f"Lösung:\n{self.wordlist.get_solution()}",
                                  font=("Terminal", 40), fg='#ebdbb2')
            label_loes.place(relx=0.5, rely=0.5, anchor="center")

        if win_condition == 6:
            for widget in self.grid_frame.winfo_children():
                widget.destroy()  # Remove all child widgets
            label = tk.Label(self.grid_frame, bg="#282828", text="GEWONNEN!", font=("Terminal", 50), fg='#98971a')
            label.place(relx=0.5, rely=0.4, anchor="center")
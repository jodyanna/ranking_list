
import tkinter as tk
import tkinter.messagebox
from dictionary import Dictionary


class GUI:
    def __init__(self, parent):
        # Initialize parent/master window
        self.parent = parent
        parent.title("My VRL")
        parent.geometry("700x600")
        parent.resizable(0, 0)

        # Instance of Dictionary class
        self.user = Dictionary()

        # Frames
        self.entry_frame = tk.Frame(parent)
        self.display_frame = tk.Frame(parent)
        self.file_functions_frame = tk.Frame(parent)

        # Labels
        self.title_entry_label = tk.Label(self.entry_frame, text="Title:")
        self.score_entry_label = tk.Label(self.entry_frame, text="Score:")
        self.title_display_label = tk.Label(self.display_frame, text="Title")
        self.score_display_label = tk.Label(self.display_frame, text="Score")
        self.file_name_entry_label = tk.Label(self.file_functions_frame, text="File name:")

        # Entry fields
        self.new_title = tk.StringVar()
        self.title_entry = tk.Entry(self.entry_frame, textvariable=self.new_title, width=30)
        self.new_score = tk.StringVar()
        self.score_entry = tk.Entry(self.entry_frame, textvariable=self.new_score, width=3)
        self.new_file_name = tk.StringVar()
        self.file_name_entry = tk.Entry(self.file_functions_frame, textvariable=self.new_file_name, width=30)

        # Buttons
        self.add_title_button = tk.Button(self.entry_frame, text="Add", width=10,
                                          command=lambda: self.add_title(self.new_title.get(), self.new_score.get()))
        self.remove_title_button = tk.Button(self.entry_frame, text="Remove", width=10,
                                             command=lambda: self.remove_title(self.new_title.get()))
        self.save_file_button = tk.Button(self.file_functions_frame, text="Save", width=10,
                                          command=lambda: self.save_file(self.new_file_name.get()))
        self.load_file_button = tk.Button(self.file_functions_frame, text="Load", width=10,
                                          command=lambda: self.load_file(self.new_file_name.get()))
        self.clear_file_button = tk.Button(self.file_functions_frame, text="Delete", width=10,
                                           command=lambda: self.delete_file(self.new_file_name.get()))

        # Text fields
        self.title_display = tk.Text(self.display_frame, background="gray75")
        self.title_display.config(state="disabled")
        self.score_display = tk.Text(self.display_frame, width=10, background="gray85")
        self.score_display.config(state="disabled")

        # Layout
        self.entry_frame.grid(padx=5, pady=10)
        self.title_entry_label.grid(row=0, column=0)
        self.title_entry.grid(row=0, column=1, columnspan=2)
        self.score_entry_label.grid(row=1, column=0)
        self.score_entry.grid(row=1, column=1, sticky="W")
        self.add_title_button.grid(row=0, column=3, rowspan=2, padx=15, sticky="EW")
        self.remove_title_button.grid(row=0, column=4, rowspan=2, padx=15, sticky="EW")

        self.display_frame.grid(padx=5, pady=1)
        self.title_display_label.grid(row=2, column=1, sticky="EW")
        self.title_display.grid(row=3, column=0, columnspan=4, padx=11, pady=2)
        self.score_display_label.grid(row=2, column=4, sticky="EW")
        self.score_display.grid(row=3, column=4, pady=2)

        self.file_functions_frame.grid(padx=5, pady=20)
        self.file_name_entry_label.grid(row=4, column=0)
        self.file_name_entry.grid(row=4, column=1)
        self.save_file_button.grid(row=5, column=0, padx=10, pady=15)
        self.load_file_button.grid(row=5, column=1, padx=10, pady=15)
        self.clear_file_button.grid(row=5, column=2, padx=10, pady=15)

    def add_title(self, new_title, new_score):
        """
        Adds Entry widgets' contents to 'user_dictionary' module.
        Clears Entry widgets; updates Text widgets.
        Show 'user_dictionary' module exception, if raised.
        """
        try:
            # Concatenate '0' onto single digit entries to prevent error in sorting
            if len(new_score) == 1:
                new_score = "0" + new_score
            self.user.add_title(new_title, new_score)

            # Clear entry fields
            self.clear_entry_fields()

            # Update text field
            self.update_text_display()

        except Exception as err:
            tkinter.messagebox.showerror(title="Error", message=err)
            self.clear_entry_fields()

    def remove_title(self, new_title):
        """
        Deletes key, value pair in 'user_dictionary' module specified by 'title_entry' widget.
        Clears Entry widgets; updates Text widgets.
        Show 'user_dictionary' module exception, if raised.
        """
        try:
            self.user.remove_title(new_title)

            # Clear entry fields
            self.clear_entry_fields()

            # Update text field
            self.update_text_display()

        except Exception as err:
            tkinter.messagebox.showerror(title="Error", message=err)
            self.clear_entry_fields()

    def save_file(self, file_name):
        """Runs 'save' method from 'user_dictionary' module."""
        try:
            self.user.save(file_name)

        except Exception as err:
            tkinter.messagebox.showerror(title="Error", message=err)
            self.clear_entry_fields()

    def load_file(self, file_name):
        """
        Runs 'load' method from 'user_dictionary' module.
        Updates Text widgets.
        """
        try:
            self.user.load(file_name)
            self.update_text_display()

        except Exception as err:
            tkinter.messagebox.showerror(title="Error", message=err)
            self.clear_entry_fields()

    def delete_file(self, file_name):
        """Runs 'delete' method from 'user_dictionary' module."""
        try:
            self.user.delete(file_name)
            self.update_text_display()
            self.clear_entry_fields()

        except Exception as err:
            tkinter.messagebox.showerror(title="Error", message=err)
            self.clear_entry_fields()

    def clear_entry_fields(self):
        """Clears text within Entry widgets."""
        for entry in (self.title_entry, self.score_entry):
            entry.delete(0, "end")

    def update_text_display(self):
        """Updates Text widgets with current key, value pairs stored in 'user_dictionary' module."""
        # Prepare text field
        self.title_display.config(state="normal")
        self.title_display.delete(0.0, "end")
        self.score_display.config(state="normal")
        self.score_display.delete(0.0, "end")

        # Insert data
        for title, score in self.user.sort_by_score():
            self.title_display.insert("insert", title + "\n")
            # Remove leading '0'
            if score.startswith("0"):
                score = score[1:]
            self.score_display.insert("insert", score + "\n")

        # Close text field
        self.title_display.config(state="disabled")
        self.score_display.config(state="disabled")


root = tk.Tk()
gui = GUI(root)
root.mainloop()

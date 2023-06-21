import tkinter as tk

from timetable import TIMETABLE
from utils import get_today, is_current_time_between


class App:
    def __init__(self):
        self._root = tk.Tk()
        self._root.resizable(False, False)
        self._root.overrideredirect(True)
        self._root.configure(bg="#D9D9D9")

        # Get the screen width
        screen_width = self._root.winfo_screenwidth()

        # Calculate the window position
        x = screen_width - 350
        y = 10

        # Set the window position and size
        self._root.geometry(f"+{x}+{y}")

        today = get_today()

        # Add a Label Frame
        self.label_frame = tk.LabelFrame(
            self._root, text=today, labelanchor="n", bg="#D9D9D9"
        )
        self.label_frame.pack(padx=10, pady=10)

        # Add a Main Frame
        self.main_frame = tk.Frame(self.label_frame, bg="#D9D9D9")
        self.main_frame.pack()

        tk.Label(self.main_frame, text="Period", bg="#D9D9D9").grid(
            row=0, column=0, ipadx=5, ipady=5
        )
        tk.Label(self.main_frame, text="Subject", bg="#D9D9D9").grid(
            row=0, column=1, ipadx=5, ipady=5
        )
        tk.Label(self.main_frame, text="Start", bg="#D9D9D9").grid(
            row=0, column=2, ipadx=5, ipady=5
        )
        tk.Label(self.main_frame, text="End", bg="#D9D9D9").grid(
            row=0, column=3, ipadx=5, ipady=5
        )

        self.widgets = []
        for idx, class_info in enumerate(TIMETABLE[today], 1):
            pno, sub, start, end = class_info

            pady = 10 if pno == "" else 0

            period_label = tk.Label(
                self.main_frame, text=str(pno), bg="#D9D9D9", relief="ridge"
            )
            period_label.grid(
                row=idx, column=0, sticky="nsew", pady=pady, ipadx=5, ipady=5
            )

            subject_label = tk.Label(
                self.main_frame, text=sub, bg="#D9D9D9", relief="ridge"
            )
            subject_label.grid(
                row=idx, column=1, sticky="nsew", pady=pady, ipadx=5, ipady=5
            )

            start_label = tk.Label(
                self.main_frame, text=start, bg="#D9D9D9", relief="ridge"
            )
            start_label.grid(
                row=idx, column=2, sticky="nsew", pady=pady, ipadx=5, ipady=5
            )

            end_label = tk.Label(
                self.main_frame, text=end, bg="#D9D9D9", relief="ridge"
            )
            end_label.grid(
                row=idx, column=3, sticky="nsew", pady=pady, ipadx=5, ipady=5
            )

            self.widgets.append((period_label, subject_label, start_label, end_label))

        self._root.bind("<Triple-Button-1>", lambda e: self._root.destroy())

        self._root.after(1000, self.highlight_current)
        self._root.mainloop()

    def highlight_current(self):
        today_timetable = TIMETABLE[get_today()]
        for idx, widgets in enumerate(self.widgets):
            if is_current_time_between(
                today_timetable[idx][2], today_timetable[idx][3]
            ):
                for widget in widgets:
                    widget.config(bg="#000000", foreground="#FFFFFF")
            else:
                for widget in widgets:
                    widget.config(bg="#D9D9D9", foreground="#000000")

        self._root.update()
        self._root.after(1000, self.highlight_current)


if __name__ == "__main__":
    App()

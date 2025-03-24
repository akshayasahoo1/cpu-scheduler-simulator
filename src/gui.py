import tkinter as tk
from tkinter import ttk

class CPUSchedulerGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("CPU Scheduler Simulator")
        self.create_widgets()

    def create_widgets(self):
        # Add input fields, buttons, etc.
        ttk.Label(self.root, text="Burst Time:").grid(row=0, column=0)
        self.burst_entry = ttk.Entry(self.root)
        self.burst_entry.grid(row=0, column=1)

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = CPUSchedulerGUI()
    app.run()

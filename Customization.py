import sqlite3
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

class FifthWindow(ttk.Toplevel):
    def __init__(self, parent, app_style, cursor, logged_in_user):
        super().__init__()
        self.parent = parent
        self.app_style = app_style
        self.cursor = cursor
        self.logged_in_user = logged_in_user
        self.geometry("500x500")
        self.title("Customization")
        self.iconbitmap("health_tracking.ico")
        self.checkbutton_var = ttk.IntVar()
        self.checkbutton_chart_var = ttk.IntVar()
        self.canvas = None
        self.create_widgets()
        self.create_layout()
        self.update_checkbutton_state()
        self.protocol("WM_DELETE_WINDOW", self.close_window)

    def create_widgets(self):
        self.label_title = ttk.Label(self, text="Customization", bootstyle="success", font=("Helvetica", 18))
        self.darkmode_checkbutton = ttk.Checkbutton(self, text="Dark Mode", variable=self.checkbutton_var,
                                                    bootstyle="success-round-toggle", onvalue=1, offvalue=0,
                                                    command=self.change_theme)
        self.chart_checkbutton = ttk.Checkbutton(self, text="Bmi Chart", variable=self.checkbutton_chart_var,
                                                 bootstyle="success", onvalue=1, offvalue=0, command=self.bmi_chart)

    def create_layout(self):
        self.label_title.pack(pady=5, anchor="center")
        self.darkmode_checkbutton.pack(padx=10, pady=40, anchor="w")
        self.chart_checkbutton.pack(padx=10, pady=30, anchor="w")

    def close_window(self):
        self.destroy()

    def change_theme(self):
        self.new_theme = "darkly" if self.app_style.theme.name == "litera" else "litera"
        self.app_style.theme_use(self.new_theme)
        self.update_checkbutton_state()

    def update_checkbutton_state(self):
        if self.app_style.theme.name == "darkly":
            self.checkbutton_var.set(1)
        else:
            self.checkbutton_var.set(0)

    def bmi_chart(self):
        if self.checkbutton_chart_var.get() == 0:
            if self.canvas:
                self.canvas.get_tk_widget().destroy()
            return

        self.cursor.execute('SELECT height, weight FROM users WHERE username=?', (self.logged_in_user,))
        user_data = self.cursor.fetchone()

        if user_data is None:
            return

        height, weight = user_data

        if not height or not weight:
            return

        bmi = weight / (height / 100) ** 2

        categories = ['Underweight', 'Normal weight', 'Overweight', 'Obesity']
        bmi_values = [18.5, 24.9, 29.9, 40]

        fig, ax = plt.subplots(figsize=(6, 4))
        ax.bar(categories, bmi_values, color='lightblue')
        ax.axhline(y=bmi, color='r', linestyle='--', label=f'Your BMI: {bmi:.2f}')
        ax.set_title('BMI Chart')
        ax.set_xlabel('BMI Categories')
        ax.set_ylabel('BMI Values')
        ax.legend()

        if self.canvas:
            self.canvas.get_tk_widget().destroy()

        self.canvas = FigureCanvasTkAgg(fig, self)
        self.canvas.get_tk_widget().pack(fill='both', expand=True)
        self.canvas.draw()

def open_main_menu(self):
    FifthWindow(self, self.app_style, self.cursor, self.logged_in_user)
import sqlite3
import ttkbootstrap as ttk
from tkinter import messagebox as msg
from tkinter import StringVar
import MainMenu


class LoginPage(ttk.Window):
    def __init__(self):
        super().__init__(themename="litera")
        self.geometry("500x500")
        self.title("Login")
        self.iconbitmap("health_tracking.ico")
        self.create_widgets()
        self.create_layout()
        self.center_window()
        self.create_db()
        self.mainloop()

    def create_widgets(self):
        self.frame_login = ttk.Labelframe(self, text="Login", bootstyle="success")
        self.username_entry = ttk.Entry(self.frame_login, width=30)
        self.username_entry.insert(0, "Username")
        self.password_entry = ttk.Entry(self.frame_login, width=30, show='*')
        self.password_entry.insert(0, "Password")
        self.login_button = ttk.Button(self.frame_login, text="Login", command=self.login, bootstyle="light")
        self.register_button = ttk.Button(self.frame_login, text="Register", command=self.register,
                                          bootstyle="light")

    def create_layout(self):
        self.frame_login.place(relx=0.5, rely=0.5, anchor="center")
        self.username_entry.pack(pady=5)
        self.password_entry.pack(pady=5)
        self.login_button.pack(pady=10)
        self.register_button.pack(pady=5)

    def create_db(self):
        self.conn = sqlite3.connect('health_tracking.db')
        self.cursor = self.conn.cursor()
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL UNIQUE,
                password TEXT NOT NULL,
                height REAL,
                weight REAL,
                steps INTEGER DEFAULT NULL,
                blood_pressure TEXT DEFAULT NULL,
                sleep_duration TEXT DEFAULT NULL
            )
        ''')
        self.conn.commit()

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if not username or not password:
            msg.showerror("Input Error", "Please enter both username and password.")
            return

        self.cursor.execute('SELECT * FROM users WHERE username=? AND password=?', (username, password))
        user = self.cursor.fetchone()

        if user:
            self.logged_in_user = username
            msg.showinfo("Login Successful", "Welcome to the Health Tracking App!")
            self.open_main_menu()
        else:
            msg.showerror("Login Error", "Invalid username or password.")

    def register(self):
        self.win_register = RegisterPage(parent=self)
        self.win_register.grab_set()

    def open_main_menu(self):
        self.main_menu = MainMenu.MainMenu(self.conn,self.cursor,self.logged_in_user)
        self.main_menu.mainloop()

    def center_window(self):
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        window_width = 500
        window_height = 500
        position_top = int(screen_height / 2 - window_height / 2)
        position_left = int(screen_width / 2 - window_width / 2)
        self.geometry(f'{window_width}x{window_height}+{position_left}+{position_top}')


class RegisterPage(ttk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.geometry("500x500")
        self.title("Register")
        self.create_widgets()
        self.create_layout()
        self.center_window()

    def create_widgets(self):
        self.frame_register = ttk.Labelframe(self, text="Register", bootstyle="success")
        self.new_username_entry = ttk.Entry(self.frame_register, width=30)
        self.new_username_entry.insert(0, "New Username")
        self.new_password_entry = ttk.Entry(self.frame_register, width=30, show='*')
        self.new_password_entry.insert(0, "New Password")
        self.weight_entry = ttk.Entry(self.frame_register, width=30)
        self.weight_entry.insert(0, "Weight (kg)")
        self.height_entry = ttk.Entry(self.frame_register, width=30)
        self.height_entry.insert(0, "Height (cm)")
        self.register_button = ttk.Button(self.frame_register, text="Register", command=self.register_user,
                                          bootstyle="light")

    def create_layout(self):
        self.frame_register.place(relx=0.5, rely=0.5, anchor="center")
        self.new_username_entry.pack(pady=5)
        self.new_password_entry.pack(pady=5)
        self.weight_entry.pack(pady=5)
        self.height_entry.pack(pady=5)
        self.register_button.pack(pady=10)

    def register_user(self):
        username = self.new_username_entry.get()
        password = self.new_password_entry.get()
        weight = self.weight_entry.get()
        height = self.height_entry.get()

        if not username or not password or not height or not weight:
            msg.showerror("Input Error", "Please fill in all fields.")
            return

        self.parent.cursor.execute('SELECT * FROM users WHERE username=?', (username,))
        existing_user = self.parent.cursor.fetchone()

        if existing_user:
            msg.showerror("Registration Error", "Username already exists.")
        else:
            self.parent.cursor.execute('INSERT INTO users (username, password, height, weight) VALUES (?, ?, ?, ?)',
                                       (username, password, height, weight))
            self.parent.conn.commit()
            msg.showinfo("Registration Successful", "User registered successfully!")
            self.destroy()

    def center_window(self):
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        window_width = 500
        window_height = 500
        position_top = int(screen_height / 2 - window_height / 2)
        position_left = int(screen_width / 2 - window_width / 2)
        self.geometry(f'{window_width}x{window_height}+{position_left}+{position_top}')


if __name__ == "__main__":
    app = LoginPage()


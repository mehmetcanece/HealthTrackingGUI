import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import DailyHealthMetrics
import Exercise
import SleepMonitoring
import Customization


class MainMenu(ttk.Toplevel):
    def __init__(self,conn,cursor,logged_in_user):
        super().__init__()
        self.conn = conn
        self.cursor = cursor
        self.logged_in_user = logged_in_user
        self.geometry("500x500")
        self.title("Main Menu")
        self.iconbitmap("health_tracking.ico")
        self.create_widgets()
        self.create_layout()
        self.mainloop()


    def create_widgets(self):
        self.frame_daily = ttk.Labelframe(self, text="Daily Health Metrics", bootstyle="success")
        self.daily_image = ttk.PhotoImage(file="daily_health.png",master=self.frame_daily)
        self.daily_image_button = ttk.Button(self.frame_daily, image=self.daily_image, command=self.open_daily_health_metrics_window,
                                             bootstyle="light")


        self.frame_exercise = ttk.Labelframe(self, text="Exercise", bootstyle="success")
        self.exercise_image = ttk.PhotoImage(file="exercise.png",master=self.frame_exercise)
        self.exercise_image_button = ttk.Button(self.frame_exercise, image=self.exercise_image, command=self.open_exercise_window,bootstyle="light")


        self.frame_sleep = ttk.Labelframe(self, text="Sleep Monitoring", bootstyle="success")
        self.sleep_image = ttk.PhotoImage(file="sleep.png",master=self.frame_sleep)
        self.sleep_image_button = ttk.Button(self.frame_sleep, image=self.sleep_image, command=self.open_sleep_monitoring_window,bootstyle="light")

        self.frame_customization = ttk.Labelframe(self, text="Customization", bootstyle="success")
        self.customization_image = ttk.PhotoImage(file="customization.png",master=self.frame_customization)
        self.customization_image_button = ttk.Button(self.frame_customization,image=self.customization_image, command=self.open_customization_window,bootstyle="light")



    def create_layout(self):
        self.columnconfigure(index=0,weight=1,uniform="eq")
        self.columnconfigure(index=1,weight=1,uniform="eq")
        self.rowconfigure(index=0,weight=1,uniform="eq")
        self.rowconfigure(index=1,weight=1,uniform="eq")
        self.rowconfigure(index=2,weight=1,uniform="eq")

        self.frame_daily.grid(column=0,row=0,padx=10,pady=10,sticky="nswe")
        self.daily_image_button.pack(pady=25)

        self.frame_exercise.grid(column=1,row=0,padx=10,pady=10,sticky="nswe")
        self.exercise_image_button.pack(pady=25)

        self.frame_customization.grid(column=0, row=1,padx=10, pady=10, sticky="nswe")
        self.customization_image_button.pack(pady=25)

        self.frame_sleep.grid(column=1,row=1,padx=10,pady=10,sticky="nswe")
        self.sleep_image_button.pack(pady=25)



    def open_daily_health_metrics_window(self):
        self.win2 = DailyHealthMetrics.SecondWindow(parent=self,conn=self.conn,cursor=self.cursor,logged_in_user=self.logged_in_user)
        self.win2.grab_set()


    def open_exercise_window(self):
        self.win3 = Exercise.ThirdWindow(parent=self)
        self.win3.grab_set()

    def open_sleep_monitoring_window(self):
        self.win4 = SleepMonitoring.FourthWindow(parent=self,conn=self.conn,cursor=self.cursor,logged_in_user=self.logged_in_user)
        self.win4.grab_set()

    def open_customization_window(self):
        self.win5 = Customization.FifthWindow(parent=self,app_style=self.style,cursor=self.cursor,logged_in_user=self.logged_in_user)
        self.win5.grab_set()













#app = MainMenu()





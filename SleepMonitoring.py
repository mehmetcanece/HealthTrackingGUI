import ttkbootstrap as ttk
from datetime import datetime,timedelta
from dateutil import parser
from tkinter import messagebox as msg
class FourthWindow(ttk.Toplevel):
    def __init__(self,parent,conn,cursor,logged_in_user):
        super().__init__()
        self.parent = parent
        self.conn = conn
        self.cursor = cursor
        self.logged_in_user = logged_in_user
        self.geometry("500x500")
        self.title("Sleep Monitoring")
        self.iconbitmap("health_tracking.ico")
        self.create_widgets()
        self.create_layout()
        self.protocol("WM_DELETE_WINDOW",self.close_window)

    def create_widgets(self):
        self.frame_bedtime = ttk.Labelframe(self, text="Bed Time",padding=10,bootstyle="success")
        self.label_bedtime = ttk.Label(self.frame_bedtime,text="Bed Time:",bootstyle="success")
        self.entry_bedtime = ttk.Entry(self.frame_bedtime,width=20)


        self.frame_wakeuptime = ttk.Labelframe(self,text="Wake Up Time",padding=10,bootstyle="success")
        self.label_wakeuptime = ttk.Label(self.frame_wakeuptime,text="Wake Up Time:",bootstyle="success")
        self.entry_wakeuptime = ttk.Entry(self.frame_wakeuptime)


        self.calculate_button = ttk.Button(self,text="Calculate Sleep",command=self.calculate_sleep,bootstyle="success")

        self.result_label = ttk.Label(self,text="",font=(16))
        self.feedback_label = ttk.Label(self,text="",font=(16))


    def create_layout(self):
        self.frame_bedtime.pack(fill="x", padx=10,pady=5)
        self.label_bedtime.pack(anchor="w", pady=2)
        self.entry_bedtime.pack(anchor="w",pady=2)

        self.frame_wakeuptime.pack(fill="x",padx=10,pady=20)
        self.label_wakeuptime.pack(anchor="w",pady=2)
        self.entry_wakeuptime.pack(anchor="w",pady=2)

        self.calculate_button.pack(anchor="e",pady=10)

        self.result_label.pack(pady=5)
        self.feedback_label.pack(pady=5)


    def close_window(self):
        self.destroy()



    def calculate_sleep(self):
        try:
            self.bedtime = self.entry_bedtime.get().strip()
            self.wakeuptime = self.entry_wakeuptime.get().strip()



            self.bedtime_dt = parser.parse(self.bedtime)
            self.wakeuptime_dt = parser.parse(self.wakeuptime)



            if self.wakeuptime_dt < self.bedtime_dt:
                self.wakeuptime_dt += timedelta(days=1)

            self.sleep_duration = self.wakeuptime_dt - self.bedtime_dt
            self.hours, self.minutes = divmod(self.sleep_duration.seconds // 60, 60)

            self.result_label.config(text=f"Sleep Duration: {self.hours} hours and {self.minutes} minutes")



            if self.hours < 6:
                self.feedback_label.config(text="Feedback: You need more sleep for better health!")
            elif self.hours > 8:
                self.feedback_label.config(text="Feedback: Great! You got plenty of rest.")
            else:
                self.feedback_label.config(text="Feedback: Your sleep duration is healthy.")

            username = self.parent.logged_in_user
            self.cursor.execute('''
                                        UPDATE users SET sleep_duration = ? WHERE username = ?
                                               ''', (self.hours, username))
            self.conn.commit()


        except ValueError as e:
            msg.showerror("Wrong Input", "Error: Invalid time format.")






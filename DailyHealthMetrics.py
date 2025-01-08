from PIL import Image
Image.CUBIC = Image.BICUBIC
import ttkbootstrap as ttk
from tkinter import messagebox as msg


class SecondWindow(ttk.Toplevel):
    def __init__(self,parent,conn,cursor,logged_in_user):
        super().__init__()
        self.parent = parent
        self.conn = conn
        self.cursor = cursor
        self.logged_in_user = logged_in_user
        self.geometry("500x500")
        self.title("Daily Health Metrics")
        self.iconbitmap("health_tracking.ico")
        self.create_widgets()
        self.create_layout()
        self.bind()
        self.protocol("WM_DELETE_WINDOW", self.close_window)



    def create_widgets(self):
        self.label_steps = ttk.Label(self, text="Steps:")
        self.meter_steps = ttk.Meter(self,metersize=150,amountused=0,amounttotal=20000,bootstyle="success",subtext="Steps",
                                     interactive=True,
                                     stripethickness=10,
                                     subtextstyle="dark")

        #self.label_weight = ttk.Label(self,text="Weight:")
        #self.entry_weight = ttk.Entry(self,bootstyle="success")

        #self.label_height = ttk.Label(self,text="Height:")
        #self.entry_height = ttk.Entry(self,bootstyle="success")

        self.label_bloodrate = ttk.Label(self,text="Blood pressure:")
        self.entry_bloodrate = ttk.Entry(self,bootstyle="success",width=20)

        self.button_calculate = ttk.Button(self,text="Feedback",bootstyle="success",command=self.feedback)


    def create_layout(self):
        self.columnconfigure(index=0,weight=1,uniform="eq")
        self.columnconfigure(index=1,weight=2,uniform="eq")
        self.rowconfigure(index=0,weight=1,uniform="eq")
        self.rowconfigure(index=1,weight=1,uniform="eq")
        self.rowconfigure(index=2,weight=1,uniform="eq")
        self.rowconfigure(index=3,weight=1,uniform="eq")
        self.rowconfigure(index=4,weight=1,uniform="eq")

        self.label_steps.grid(column=0,row=0,padx=10,pady=(10,0))
        self.meter_steps.grid(column=1,row=0,rowspan=2)
        #self.label_weight.grid(column=0,row=1,padx=10,pady=(10,0))
        #self.entry_weight.grid(column=1,row=1,sticky="we")
        #self.label_height.grid(column=0,row=2,padx=10,pady=(10,0))
        #self.entry_height.grid(column=1,row=2,sticky="we")
        self.label_bloodrate.grid(column=0,row=3,padx=10,pady=(10,0))
        self.entry_bloodrate.grid(column=1,row=3)
        self.button_calculate.grid(column=1,row=4,columnspan=2,sticky="e")



    def close_window(self):
        self.destroy()


    def feedback(self,event=None):
        try:
            feedback = []

            steps = int(self.meter_steps["amountused"])
            blood_pressure = self.entry_bloodrate.get()
            if "/" not in blood_pressure or len(blood_pressure.split("/")) != 2:
                raise ValueError("Invalid blood pressure format. Use 'SYS/DIA'.")

            sys_bp, dia_bp = map(int, blood_pressure.split("/"))

            if steps < 5000:
                feedback.append("Steps: Try to walk more! Aim for at least 5000 steps daily.")
            elif steps < 10000:
                feedback.append("Steps: Good effort! Try reaching 10000 steps for better health.")
            else:
                feedback.append("Steps: Excellent! Keep up the great activity level.")


            if sys_bp < 90 or dia_bp < 60:
                feedback.append("BP: Your blood pressure is too low.")
            elif sys_bp > 140 or dia_bp > 90:
                feedback.append("BP: Your blood pressure is too high.")
            else:
                feedback.append("BP: Your blood pressure is normal.")

            username = self.parent.logged_in_user
            self.cursor.execute('''
                        UPDATE users SET steps = ?, blood_pressure = ? WHERE username = ?
                    ''', (steps, blood_pressure, username))
            self.conn.commit()

            msg.showinfo("Health Feedback", "\n".join(feedback))

        except ValueError as e:
            msg.showerror("Input Error", str(e))


    def bind(self):
        self.entry_bloodrate.bind("<Return>", self.feedback)










import ttkbootstrap as ttk

class ThirdWindow(ttk.Toplevel):
    def __init__(self,parent):
        super().__init__()
        self.parent = parent
        self.geometry("500x500")
        self.title("Exercise")
        self.iconbitmap("health_tracking.ico")
        self.create_widgets()
        self.create_layout()
        self.protocol("WM_DELETE_WINDOW",self.close_window)


    def create_widgets(self):
        self.exercise_notebook = ttk.Notebook(self,bootstyle="dark")
        self.tab1 = ttk.Frame(self.exercise_notebook)
        self.tab2 = ttk.Frame(self.exercise_notebook)
        self.tab3 = ttk.Frame(self.exercise_notebook)
        self.label_title = ttk.Label(self,text="Exercise Plans", font=("Helvetica",18), bootstyle="success")
        self.label_exercise1 = ttk.Label(self.tab1,text="Cardio Plan:\n- Warm up: 10 minutes\n- Walking on a treadmill: 10 minutes\n- A slow bike ride: 20 minutes\n- A relaxed swim: 20 minutes",anchor="w",justify="left")
        self.label_exercise2 = ttk.Label(self.tab2,text="Strength:\n- Dumbbell Curl: 3x12\n- Plank: 40 second\n- Squat: 3x20\n- Crunches: 3x15\n- Dumbbell Shoulder Press: 3x12", anchor="w", justify="left")
        self.label_exercise3 = ttk.Label(self.tab3,text="Yoga:\n- Mountain Pose(Tadasana): Hold for 5 full breaths\n- Tree Pose(Vrksasana): Hold for 5 full breaths\n- High Lunge: Hold for 5 full breaths\n- Baby Cobra: Relax, exhale, and repeat for 5 full breaths.", anchor="w", justify="left")

    def create_layout(self):
        self.label_title.pack(pady=20)
        self.exercise_notebook.pack(pady=20,fill="y",expand=True)
        self.label_exercise1.pack(pady=20)
        self.label_exercise2.pack(pady=20)
        self.label_exercise3.pack(pady=20)
        self.exercise_notebook.add(self.tab1,text="Cardio Plan")
        self.exercise_notebook.add(self.tab2,text="Strength")
        self.exercise_notebook.add(self.tab3,text="Yoga")

    def close_window(self):
        self.destroy()

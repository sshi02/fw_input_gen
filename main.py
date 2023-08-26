import tkinter as tk        # GUI Library, native Python library
from tkinter import ttk     # extra widgets from library
import os                   # help with PATH

#### main.py structure:
# Helper Classes, such as Classes that manage widgets
# Helper Functions
# Main GUI Body
#   - This contains a generate() function for generating input.txt

#### Helper Classes
class LabelEntryD: # shorthand LED in variable names
    '''LabelEntryD(ecimal) Class. 
    This class manages a label and entry widget, where input to the
    entry is validated and kept to integer values.

    Args:
        m: Frame/Window the widgets will belong to
        text: Label text
    Methods:
        set(): sets value of entry
        get(): returns last validated value inputted to entry
    
    Example use case:
    |   import tkinter as tk
    |
    |   m = tk.Tk()                               # init tkinter window
    |   height_led = LabelEntryD(m, "Height (m)") # Make LED for Height value
    |   height_led.set(15)                        # Make default value 15
    |   print(height_led.get())                   # Get current value of LED
    |   height_led.grid(row = 0, column = 0)      # Place and position LED in window
    |   m.mainloop()
    '''
    def __init__(self, m, text) -> None:
        self.value = 0
        self.label = tk.Label(m, text = text)
        self.str = tk.StringVar(value = f"{self.value : .0f}")
        def set(var, index, mode):
            if (self.str.get().strip().isdigit()):
                self.value = int(self.str.get())
            elif not self.str.get().strip() == '':
                self.str.set(f"{self.value : .0f}")
            return True
        self.str.trace_add("write", set)
        self.entry = tk.Entry(m, textvariable = self.str)
    def set(self, x):
        self.str.set(f"{x : .0f}")
        self.value = x
    def get(self):
        return self.value
    def hide(self):
        self.label.grid_forget()
        self.label.pack_forget()
        self.entry.grid_forget()
        self.label.pack_forget()
    def grid(self, row = 0, column = 0):
        self.label.grid(row = row, column = column)
        self.entry.grid(row = row, column = column + 1)
            
class LabelEntryF:
    '''LabelEntryF(loat) Class. 
    This class manages a label and entry widget, where input to the
    entry is validated and kept to float values.

    Args:
        m: Frame/Window the widgets will belong to
        text: Label text
    Methods:
        set(): sets value of entry
        get(): returns last validated value inputted to entry
    
    Example use case:
    |   import tkinter as tk
    |
    |   m = tk.Tk()                               # init tkinter window
    |   height_lef = LabelEntryD(m, "Height (m)") # Make LEF for Height value
    |   height_lef.set(15.0)                      # Make default value 15.0
    |   print(height_lef.get())                   # Get current value of LEF
    |   height_lef.grid(row = 0, column = 0)      # Place and position LEF in window
    |   m.mainloop()
    '''
    def __init__(self, m, text) -> None:
        self.value = 0.0
        self.label = tk.Label(m, text = text)
        self.str = tk.StringVar(value = f"{self.value : f}")
        def set(var, index, mode):
            if (self.str.get().strip().replace(".", "", 1).replace("-", "", 1).isnumeric()):
                self.value = float(self.str.get())
            elif not self.str.get().strip() == "":
                self.str.set(f"{self.value : f}")
            return True
        self.str.trace_add("write", set)
        self.entry = tk.Entry(m, textvariable = self.str)
        
    def set(self, x):
        self.str.set(f"{x : f}")
        self.value = x
    def get(self):
        return self.value
    def hide(self):
        self.label.grid_forget()
        self.label.pack_forget()
        self.entry.grid_forget()
        self.entry.pack_forget()
    def grid(self, row = 0, column = 0):
        self.label.grid(row = row, column = column)
        self.entry.grid(row = row, column = column + 1)

class LabelEntryS:
    '''LabelEntryS(tring) Class. 
    This class manages a label and entry widget. Input is not validated

    Args:
        m: Frame/Window the widgets will belong to
        text: Label text
    Methods:
        set(): sets value of entry
        get(): returns last value inputted to entry
    
    Example use case:
    |   import tkinter as tk
    |
    |   m = tk.Tk()                               # init tkinter window
    |   name_les = LabelEntryS(m, "Name")         # Make LEF for Height value
    |   name_les.set("David")                     # Make default value 15.0
    |   print(name_les.get())                     # Get current value of LEF
    |   name_les.grid(row = 0, column = 0)
    |   m.mainloop()
    '''
    def __init__(self, m, text) -> None:
        self.label = tk.Label(m, text = text)
        self.str = tk.StringVar(value = "")
        self.entry = tk.Entry(m, textvariable = self.str)
        
    def set(self, x):
        self.str.set(x)
    def get(self):
        return self.str.get()
    def hide(self):
        self.label.grid_forget()
        self.label.pack_forget()
        self.entry.grid_forget()
        self.entry.pack_forget()
    def grid(self, row = 0, column = 0):
        self.label.grid(row = row, column = column)
        self.entry.grid(row = row, column = column + 1)

class CheckB:
    def __init__(self, m, text, value = False, command = None) -> None:
        self.bool = tk.BooleanVar(value = value)
        if command != None:
            self.check = tk.Checkbutton(m, text = text,
                                    variable = self.bool,
                                    onvalue = True,
                                    offvalue = False,
                                    command = command)
        else: 
            self.check = tk.Checkbutton(m, text = text,
                                    variable = self.bool,
                                    onvalue = True,
                                    offvalue = False)            

            
    def set(self, x):
        self.bool.set()
    def get(self):
        return self.bool.get()
    def hide(self):
        self.check.grid_forget()
        self.check.pack_forget()
    def grid(self, row = 0, column = 0):
        self.check.grid(row = row, column = column)

class CreateToolTip(object): # shortened to ttp in var names
    """
    Create a tooltip for a given widget, so when user hovers over a widget, a textbox/tooltip
    will appear.

    Args:
        widget: The widget to be assigned a tooltip
        text:   Text to display when tooltip shows

    Example use case:
    import tkinter as tk
    |   m = tk.Tk()                                     # init tkinter window
    |   heading = tk.Label(m, text = "Potato Soup")     # init Label Widget
    |   heading_ttp = CreateToolTip(heading,            # Create tooltip with text:
    |                               "Serves 5 people")  # <---
    |   heading.pack()                                  # Pack into window, no need
    |   m.mainloop()                                    # to place/position the ttp
    """
    def __init__(self, widget, text='widget info'):
        self.waittime = 500     #miliseconds
        self.wraplength = 180   #pixels
        self.widget = widget
        self.text = text
        self.widget.bind("<Enter>", self.enter)
        self.widget.bind("<Leave>", self.leave)
        self.widget.bind("<ButtonPress>", self.leave)
        self.id = None
        self.tw = None
    def enter(self, event=None):
        self.schedule()
    def leave(self, event=None):
        self.unschedule()
        self.hidetip()
    def schedule(self):
        self.unschedule()
        self.id = self.widget.after(self.waittime, self.showtip)
    def unschedule(self):
        id = self.id
        self.id = None
        if id:
            self.widget.after_cancel(id)
    def showtip(self, event=None):
        x = y = 0
        x, y, cx, cy = self.widget.bbox("insert")
        x += self.widget.winfo_rootx() + 25
        y += self.widget.winfo_rooty() + 20
        # creates a toplevel window
        self.tw = tk.Toplevel(self.widget)
        # Leaves only the label and removes the app window
        self.tw.wm_overrideredirect(True)
        self.tw.wm_geometry("+%d+%d" % (x, y))
        label = tk.Label(self.tw, text=self.text, justify='left',
                       background="#ffffff", relief='solid', borderwidth=1,
                       wraplength = self.wraplength)
        label.pack(ipadx=1)
    def hidetip(self):
        tw = self.tw
        self.tw= None
        if tw:
            tw.destroy()

### Helper Functions

def center(e):
    '''
    This function is used to center the title of the window
    '''
    w = int(m.winfo_width() / 3.5)
    s = 'Generate input.txt'.rjust(w//2)
    m.title(s)

# unique filename func
def uniquify(path):
    '''
    This function is used to produce a unique filename given a PATH
    For example, if given input.txt and an input.txt already exists,
    the return is a path for input(1).txt
    '''
    filename, extension = os.path.splitext(path)
    counter = 1
    while os.path.exists(path):
        path = filename + "(" + str(counter) + ")" + extension
        counter += 1
    return path

### main body
if __name__ == "__main__":      # Stops bad run of main.py
    m = tk.Tk()
    cwd = os.path.dirname(os.path.realpath(__file__))
    log_title = "model1"
    output_folder = "output/"
    init_station = tk.BooleanVar(value = False)


    # Local Functions
    # TODO: hotstart, pbc, wavemaker, title
    def generate():
        print("Generating input.txt")
        if overwrite_cb.get():
            filename = os.path.join(cwd, "input.txt")
        else:
            filename = uniquify(os.path.join(cwd, "input.txt"))
        f = open(filename, "w+")
        f.write("! INPUT FILE FOR FUNWAVE_TVD\n! NOTE: all input parameter are capital sensitive\n")
        f.write("! --------------------TITLE-------------------------------------\n! title only for log file\n")
        f.write(f"TITLE ={log_title}\n\n")
        f.write("! -------------------PARALLEL INFO-----------------------------\n!    PX,PY - processor numbers in X and Y\n!    NOTE: make sure consistency with mpirun -np n (px*py)\n")
        f.write(f"PX ={px_led.get() : .0f}\nPY ={py_led.get() : .0f}\n")
        f.write("! --------------------DEPTH-------------------------------------\n! Depth types, DEPTH_TYPE=DATA: from depth file\n!              DEPTH_TYPE=FLAT: idealized flat, need depth_flat\n!              DEPTH_TYPE=SLOPE: idealized slope,\n!                                 need slope,SLP starting point, Xslp\n!                                 and depth_flat\n")
        f.write(f"DEPTH_TYPE ={last_depth_check}\n")
        if "FLAT" in last_depth_check or "SLOPE" in last_depth_check:
                f.write(f"DEPTH_FLAT ={depth_flat_lef.get() : f}\n")
                if "SLOPE" in last_depth_check:
                    f.write(f"SLP ={slope_lef.get() : f}\nXslp ={xslope_lef.get() : f}\n")
        else:
            f.write(f"DEPTH_FILE = {depth_data.get()}\n")
        f.write("! -------------------PRINT---------------------------------\n! PRINT*,\n! result folder\n")
        f.write(f"RESULT_FOLDER = {output_folder}\n")
        f.write("! ------------------DIMENSION-----------------------------\n! global grid dimension\n")
        f.write(f"Mglob = {mglob_led.get()}\nNglob = {nglob_led.get()}\n")
        f.write("! ----------------- TIME----------------------------------\n! time: total computational time/ plot time / screen interval\n! all in seconds\n")
        f.write(f"TOTAL_TIME ={time_total_lef.get() : f}\n")
        f.write(f"PLOT_INTV ={plot_int_lef.get() : f}\n")
        f.write(f"SCREEN_INTV ={screen_int_lef.get() : f}\n")
        if (hotstart_check.get()):
            pass
        f.close()

    # Window Params
    m.geometry("1400x600")
    m.bind("<Configure>", center)

    # Frames
    title_frame = tk.Frame(m)
    parallel_frame = tk.Frame(m)
    dimension_frame = tk.Frame(m)
    time_frame = tk.Frame(m)
    depth_frame = tk.Frame(m)
    physics_frame = tk.Frame(m)
    numerics_frame = tk.Frame(m)
    hotstart_frame = tk.Frame(m)
    init_frame = tk.Frame(m)
    sponge_frame = tk.Frame(m)
    wavemaker_frame = tk.Frame(m)
    pbc_frame = tk.Frame(m)
    warnings_frame = tk.Frame(m)
    igp_frame = tk.Frame(m)
    # column 0
    title_frame.grid(row = 0, 
                     sticky = "NW", pady = 5)
    parallel_frame.grid(row = 2, column = 0, 
                        sticky = "NW", pady = 5)
    dimension_frame.grid(row = 3, column = 0, 
                         sticky = "NW", pady = 5)
    time_frame.grid(row = 4, column = 0, 
                    sticky = "NW", pady = 5)
    depth_frame.grid(row = 5, column = 0, 
                     sticky = "NW", pady = 5)
    # column 1
    physics_frame.grid(row = 0, column = 1, 
                  rowspan = 5, sticky = "NW")
    # column 2
    pbc_frame.grid(row = 0, column = 2, sticky = "SW")
    wavemaker_frame.grid(row = 1, column = 2, rowspan = 8, sticky = "NW")
    # column 3
    hotstart_frame.grid(row = 0, column = 3, 
                        rowspan = 3, sticky = "NW")
    init_frame.grid(row = 3, column = 3,
                    rowspan = 2, sticky = "NW")
    # column max
    warnings_frame.grid(row = 2, column = 8, 
                        rowspan = 4)
    igp_frame.grid(row = 9, column = 8, sticky = "SW")
    
    # row column weigthing system
    m.columnconfigure(0, weight = 1)
    m.columnconfigure(1, weight = 1)
    m.columnconfigure(2, weight = 1)
    m.rowconfigure(8, weight = 1)
    # Title Widgets
    title_les = LabelEntryS(title_frame, "Log Title")
    title_les.set("model1")
    title_les.grid(row = 0)
    # Parallel Widgets
    parallel_label = tk.Label(parallel_frame, text = "Parallelization Arguments")
    px_led = LabelEntryD(parallel_frame, "PX")
    py_led = LabelEntryD(parallel_frame, "PY")
    px_led.set(os.cpu_count() / 2)
    py_led.set(1)
    # parallel pos
    parallel_label.grid(row = 0, columnspan = 3, sticky = "W")
    px_led.entry.configure(width = 5)
    py_led.entry.configure(width = 5)
    px_led.grid(row = 1, column = 0)
    py_led.grid(row = 1, column = 2)
    # ttp
    parallel_label_ttp = CreateToolTip(parallel_label, "PX, PY - Processor Numbers in X\nNOTE: Correlates to mpirun -np n (px*py)")
    px_led_ttp = CreateToolTip(px_led.label, "PX - Processor Numbers in X")
    py_led_ttp = CreateToolTip(py_led.label, "PY - Processor Numbers in Y")

    # Dimension/Grid Widgets
    dimension_label = tk.Label(dimension_frame, text = "Dimension and Grid Size Arguments")
    mglob_led = LabelEntryD(dimension_frame, "Mglob")
    nglob_led = LabelEntryD(dimension_frame, "Nglob")
    dx_lef = LabelEntryF(dimension_frame, "dx (m)")
    dy_lef = LabelEntryF(dimension_frame, "dy (m)")
    mglob_led.set(0)
    nglob_led.set(0)
    dx_lef.set(1.0)
    dy_lef.set(1.0)
    # dimension pos
    dimension_label.grid(row = 0, columnspan = 2, sticky = "W")
    mglob_led.grid(row = 1, column = 0)
    nglob_led.grid(row = 2, column = 0)
    dx_lef.grid(row = 3, column = 0)
    dy_lef.grid(row = 4, column = 0)

    # Time Widgets
    time_label = tk.Label(time_frame, text = "Time Arguments")
    time_total_lef = LabelEntryF(time_frame, "Total Time (s)")
    plot_int_lef = LabelEntryF(time_frame, "Output Interval (s)")
    screen_int_lef = LabelEntryF(time_frame, text = "Console Interval (s)")
    plot_start_lef = LabelEntryF(time_frame, "Output Start Time (s)")
    def onCheckFixedDt():
        if fixed_dt_check.get():
            show_dt()
        else:
            hide_dt()
    fixed_dt_check = CheckB(time_frame, text = "Fixed dt",
                       value = False, command = onCheckFixedDt)
    dt_lef = LabelEntryF(time_frame, 'dt (s)')
    time_total_lef.set(300.0)
    plot_int_lef.set(1.0)
    screen_int_lef.set(1.0)
    plot_start_lef.set(0.0)
    dt_lef.set(1.0)
    # time pos
    time_label.grid(row = 0, columnspan = 2, sticky = "W")
    time_total_lef.grid(row = 1, column = 0)
    plot_int_lef.grid(row = 2, column = 0)
    screen_int_lef.grid(row = 3, column = 0)
    plot_start_lef.grid(row = 4, column = 0)
    fixed_dt_check.check.grid(row = 5, column = 0, sticky = "W")

    def show_dt():
        dt_lef.grid(row = 6, column = 0)
    def hide_dt():
        dt_lef.hide()

    # Depth Widgets
    def onCheckDepth():
        global last_depth_check
        if 'FLAT' in last_depth_check:
            isFlat.set(False)
            if not (isSlope.get() or isDepthData.get()):
                isFlat.set(True)
                return
        elif 'SLOPE' in last_depth_check:
            isSlope.set(False)
            if not (isFlat.get() or isDepthData.get()):
                isSlope.set(True)
                return
        else:
            isDepthData.set(False)
            if not (isFlat.get() or isSlope.get()):
                isDepthData.set(True)
                return
        hide_depth_entries()
        if isFlat.get():
            last_depth_check = 'FLAT'
            show_flat_lef()
        elif isSlope.get():
            last_depth_check = 'SLOPE'
            show_slope_lef()
        elif isDepthData.get():
            last_depth_check = 'DATA'
            show_data()
    # widget vars
    last_depth_check = 'FLAT'
    isFlat = tk.BooleanVar(value = True)
    isSlope = tk.BooleanVar(value = False)
    isDepthData = tk.BooleanVar(value = False)
    depth_data = tk.StringVar(value = "depth.txt")
    # widgets
    depth_label = tk.Label(depth_frame, text = "Depth Type")
    flat_check = tk.Checkbutton(depth_frame, text = "Flat", 
                                variable = isFlat, command = onCheckDepth)
    slope_check = tk.Checkbutton(depth_frame, text = "Slope", 
                                 variable = isSlope, command = onCheckDepth)
    depth_data_check = tk.Checkbutton(depth_frame, text = "Data",
                                variable = isDepthData, command = onCheckDepth)
    depth_flat_lef = LabelEntryF(depth_frame, "Depth (m)")
    slope_lef = LabelEntryF(depth_frame, "Slope")
    xslope_lef = LabelEntryF(depth_frame, "X Pos (m)")
    depth_data_les = LabelEntryS(depth_frame, " File name")
    depth_flat_lef.set(10.0)     
    slope_lef.set(0.05)
    xslope_lef.set(400)
    # depth pos
    depth_label.grid(row = 1, columnspan = 2, sticky = "W")
    flat_check.grid(row = 2, column = 0, sticky = "W")
    slope_check.grid(row = 3, column = 0, sticky = "W")
    depth_data_check.grid(row = 4, column = 0, sticky = "W")
    depth_flat_lef.grid(row = 2, column = 1)
    # support funcs
    def show_flat_lef():
        depth_flat_lef.grid(row = 2, column = 1)
    def show_slope_lef():
        depth_flat_lef.grid(row = 2, column = 1)
        slope_lef.grid(row = 3, column = 1)
        xslope_lef.grid(row = 4, column = 1)
    def show_data():
        depth_data_les.grid(row = 2, column = 1)
    def hide_depth_entries():
        depth_flat_lef.hide()
        slope_lef.hide()
        xslope_lef.hide()
        depth_data_les.hide()
        pass
    
    # Physics Widgets
    physics_label = tk.Label(physics_frame, text = "Physics Arguments")
    dispersion_check = CheckB(physics_frame, "Dispersion",
                              value = True)
    gamma1_lef = LabelEntryF(physics_frame, "Gamma1")
    gamma2_lef = LabelEntryF(physics_frame, "Gamma2")
    gamma3_lef = LabelEntryF(physics_frame, "Gamma3")
    beta_lef = LabelEntryF(physics_frame, text = "Beta")
    def onCheckViscosityBreaking():
        if viscosity_breaking_check.get():
            show_breaking_entries()
        else:
            hide_breaking_entries()
    viscosity_breaking_check = CheckB(physics_frame, text = "Viscosity Breaking",
                                      value = False, command = onCheckViscosityBreaking)
    cbrk1_lef = LabelEntryF(physics_frame, text = "c1")
    cbrk2_lef = LabelEntryF(physics_frame, text = "c2")
    swe_eta_lef = LabelEntryF(physics_frame, text = "Ratio for NSWE")
    roller_effect_check = CheckB(physics_frame, text = "Roller Effect",
                                 value = False)
    friction_label = tk.Label(physics_frame, text = "Friction Specification")
    def onCheckFrictionMatrix():
        if friction_matrix_check.get():
            friction_matrix_les.grid(row = 14)
        else:
            friction_matrix_les.hide()

    friction_matrix_check = CheckB(physics_frame, text = "Friction Matrix",
                                   command = onCheckFrictionMatrix)
    friction_matrix_les = LabelEntryS(physics_frame, text = "Matrix File")
    cd_fixed_lef = LabelEntryF(physics_frame, text = "Bottom Friction Coef")
    show_breaking_check = CheckB(physics_frame, text = "Calculate Breaking Index")

    gamma1_lef.set(1.0)
    gamma2_lef.set(1.0)
    gamma3_lef.set(1.0)
    beta_lef.set(-0.531)
    cbrk1_lef.set(0.45)
    cbrk2_lef.set(0.35)
    swe_eta_lef.set(0.8)

    physics_label.grid(row = 0, columnspan = 2, sticky = "W")
    dispersion_check.check.grid(row = 1, sticky = "W")
    gamma1_lef.grid(row = 2)
    gamma2_lef.grid(row = 3)
    gamma3_lef.grid(row = 4)
    beta_lef.grid(row = 5)
    swe_eta_lef.grid(row = 6)
    roller_effect_check.check.grid(row = 7, sticky = "W")
    viscosity_breaking_check.check.grid(row = 8, sticky = "W")
    def show_breaking_entries():
        cbrk1_lef.grid(row = 9)
        cbrk2_lef.grid(row = 10)
    def hide_breaking_entries():
        cbrk1_lef.hide()
        cbrk2_lef.hide()
    friction_label.grid(row = 11, sticky = "W")
    cd_fixed_lef.grid(row = 12)
    friction_matrix_check.check.grid(row = 13, sticky = "W")
        
    # Hot Start
    def onCheckHotStart():
        if hotstart_check.get():   
            show_hotstart_entries()
        else:
            hide_hotstart_entries()
    hotstart_check = CheckB(hotstart_frame, "Hot Start",
                        value = False, command = onCheckHotStart)
    filenum_hot_led = LabelEntryD(hotstart_frame, 
                                  "Initial Enumeration")
    hotstart_int_lef = LabelEntryF(hotstart_frame,
                                  "Hot Start Time (s)")
    hotstart_check.check.grid(row = 0, sticky = "W")
    def show_hotstart_entries():
        filenum_hot_led.grid(row = 1)
        hotstart_int_lef.grid(row = 2)
    def hide_hotstart_entries():
        filenum_hot_led.hide()
        hotstart_int_lef.hide()

    # Initial Condition
    def onCheckInit():
        if init_check.get():
            show_init_entries()
        else:
            hide_init_entries()
    def onCheckInitMask():
        if init_mask_check.get():
            show_init_mask_entry()
        else:
            hide_init_mask_entry()
    init_check = CheckB(init_frame, "Initial Condition",
                        value = False, command = onCheckInit)
    init_eta_les = LabelEntryS(init_frame, "Initial Eta File")
    init_u_les = LabelEntryS(init_frame, "Initial U File")
    init_v_les = LabelEntryS(init_frame, "Initial V File")
    init_mask_check = CheckB(init_frame, "Initial Mask",
                             value = False, command = onCheckInitMask)
    init_mask_les = LabelEntryS(init_frame, "Mask File")
    
    init_check.check.grid(row = 0, columnspan = 2, sticky = "NW")
    def show_init_entries():
        init_u_les.grid(row = 1)
        init_v_les.grid(row = 2)
        init_mask_check.grid(row = 3)
    def hide_init_entries():
        init_u_les.hide()
        init_v_les.hide()
        init_mask_check.hide()
        init_mask_les.hide()
    def show_init_mask_entry():
        init_mask_les.grid(row = 4)
        print("show")
    def hide_init_mask_entry():
        init_mask_les.hide()
    
    # Wavemaker widgets
    isWavemaker = tk.BooleanVar(value = False)
    wavemaker = "WK_REG"
    wavemaker_var = tk.Variable(value = ('Internal Wave Maker (WK_REG)', 'TMA Spectrum Wave Maker (WK_IRR)',
                        'Spectrum w/ Wave Coherence (WK_NEW_IRR)', 'JONSWAP Spectrum Wave Maker (JON_2D)',
                        'JONSWAP 1D Spectrum Wave Maker (JON_1D)', 'TMA 1D Spectrum Wave Maker (TMA_1D)',                
                        'Wave Maker Time Series (WK_TIME_SERIES)', '2D Spectrum Data (WK_DATA2D)', 
                        '2D Wave Data (WK_NEW_DATA_2D)', 'Left Boundary Wave Maker (LEFT_BC_IRR)',
                        'Left Boundary Solitary (LEF_SOL)', 'Initial Solitary Wave (INI_SOL)', 
                        'Rectangular Hump (INI_REC)', 'Initial Gaussian Hump (INI_GAU)'))
    def onCheckWaveMaker():
        if (isWavemaker.get()):
            show_wavemaker()
        else:
            hide_wavemaker()
    wavemaker_check = tk.Checkbutton(wavemaker_frame, text = "Wave Maker",
                                     variable = isWavemaker, command = onCheckWaveMaker)
    wavemaker_list = tk.Listbox(wavemaker_frame, listvariable = wavemaker_var,
                                selectmode = tk.SINGLE, height = 4, width = 42)
    wavemaker_scrollbar = ttk.Scrollbar(wavemaker_frame, orient = tk.VERTICAL,
                                        command = wavemaker_list.yview)
    wavemaker_list['yscrollcommand'] = wavemaker_scrollbar
    # wavemaker Params
    wavemaker_break_lef = LabelEntryF(wavemaker_frame, text = "Breaking Parameter")
    xc_wk_lef = LabelEntryF(wavemaker_frame, text = "X (m)")
    yc_wk_lef = LabelEntryF(wavemaker_frame, text = "Y (m)")
    ywidth_wk_lef = LabelEntryF(wavemaker_frame, text = "Y Width (m)")
    tperiod_lef = LabelEntryF(wavemaker_frame, text = "Period (s)")
    amp_wk_lef = LabelEntryF(wavemaker_frame, text = "Amplitude (m)")
    dep_wk_lef = LabelEntryF(wavemaker_frame, text = "Water Depth (m)")
    theta_wk_lef = LabelEntryF(wavemaker_frame, text = "Theta (deg)")
    time_ramp_lef = LabelEntryF(wavemaker_frame, text = "Time Ramp (s)")
    freqpeak_lef = LabelEntryF(wavemaker_frame, text = "Peak Freq (1/s)")
    delta_wk_lef = LabelEntryF(wavemaker_frame, text = "Delta")
    freqmin_lef = LabelEntryF(wavemaker_frame, text = "Min Freq (1/s)")
    freqmax_lef = LabelEntryF(wavemaker_frame, text = "Max Freq (1/2)")
    hmo_lef = LabelEntryF(wavemaker_frame, text = "Hmo (m)")
    gamma_tma_lef = LabelEntryF(wavemaker_frame, text = "Gamma")
    theta_peak_lef = LabelEntryF(wavemaker_frame, text = "Theta Peak")
    nfreq_led = LabelEntryD(wavemaker_frame, text = "Num Freq")
    ntheta_led = LabelEntryD(wavemaker_frame, text = "Num Theta")
    equal_energy = tk.BooleanVar(value = False)
    equal_energy_check = tk.Checkbutton(wavemaker_frame, text = "Equal Energy",
                                        variable = equal_energy)
    wavemaker_list.select_set(0)
    wavemaker_break_lef.set(cbrk1_lef.get())
    gamma_tma_lef.set(3.3)
    theta_peak_lef.set(0.0)
    nfreq_led.set(45)
    ntheta_led.set(24)

    # use Default Checkbutton
    use_defaults_wk = tk.BooleanVar(value = True)
    def toggle_defaults_wk():
        toggle_wavemaker_entries(None)
    use_defaults_wk_check = tk.Checkbutton(wavemaker_frame, text = "Use Defaults",
                                           variable = use_defaults_wk, command = toggle_defaults_wk)
    # wavemaker pos
    wavemaker_check.grid(row = 0, columnspan = 2, sticky = tk.N + tk.W)
    def show_wavemaker():
        wavemaker_break_lef.grid(row = 1)
        wavemaker_list.grid(row = 2, columnspan = 2)
        wavemaker_scrollbar.grid(row = 2, column = 3, sticky = "NSE")
        toggle_wavemaker_entries("")
    def hide_wavemaker():
        wavemaker_break_lef.hide()
        wavemaker_list.grid_forget()
        wavemaker_scrollbar.grid_forget()
        hide_wavemaker_entries()
    def hide_wavemaker_entries():
        use_defaults_wk_check.grid_forget()
        use_defaults_wk_check.pack_forget()
        xc_wk_lef.hide()
        yc_wk_lef.hide()
        ywidth_wk_lef.hide()
        tperiod_lef.hide()
        amp_wk_lef.hide()
        dep_wk_lef.hide()
        theta_wk_lef.hide()
        time_ramp_lef.hide()
        delta_wk_lef.hide()
        freqpeak_lef.hide()
        freqmin_lef.hide()
        freqmax_lef.hide()
        hmo_lef.hide()
        gamma_tma_lef.hide()
        theta_peak_lef.hide()
        nfreq_led.hide()
        ntheta_led.hide()
        equal_energy_check.grid_forget()
        use_defaults_wk_check.grid_forget()
    def toggle_wavemaker_entries(event):
        global wavemaker
        hide_wavemaker_entries()
        curwavemaker = wavemaker_list.get(wavemaker_list.curselection()[0])
        if 'WK_REG' in curwavemaker:
            wavemaker = 'WK_REG'
            xc_wk_lef.grid(row = 3)
            yc_wk_lef.grid(row = 4)
            ywidth_wk_lef.grid(row = 5)
            tperiod_lef.grid(row = 6)
            amp_wk_lef.grid(row = 7)
            dep_wk_lef.grid(row = 8)
            theta_wk_lef.grid(row = 9)
            time_ramp_lef.grid(row = 10)
        elif 'WK_IRR' in curwavemaker:
            wavemaker = 'WK_IRR'
            xc_wk_lef.grid(row = 3)
            yc_wk_lef.grid(row = 4)
            ywidth_wk_lef.grid(row = 5)
            dep_wk_lef.grid(row = 6)
            time_ramp_lef.grid(row = 7)
            delta_wk_lef.grid(row = 8)
            freqpeak_lef.grid(row = 9)
            freqmin_lef.grid(row = 10)
            freqmax_lef.grid(row = 11)
            hmo_lef.grid(row = 12)
            use_defaults_wk_check.grid(row = 13)
            if not use_defaults_wk.get():
                gamma_tma_lef.grid(row = 14)
                theta_peak_lef.grid(row = 15)
                nfreq_led.grid(row = 16)
                ntheta_led.grid(row = 17)
                equal_energy_check.grid(row = 18)
        elif 'WK_NEW_IRR' in curwavemaker:
            wavemaker = 'WK_NEW_IRR'
            pass
        elif 'JON_2D' in curwavemaker:
            wavemaker = "JON_2D"
            pass
        elif 'JON_1D' in curwavemaker:
            wavemaker = "JON_1D"
            pass
        elif 'TMA_1D' in curwavemaker:
            wavemaker = "TMA_1D"
            pass
        elif 'WK_NEW_DATA_2D' in curwavemaker:
            wavemaker = "WK_NEW_DATA_2D"
            pass
        elif 'WK_DATA2D' in curwavemaker:
            wavemaker = "WK_DATA2D"
        elif 'WK_NEW_DATA_2D' in curwavemaker:
            wavemaker = 'WK_NEW_DATA_2D'
        elif 'LEFT_BC_IRR' in curwavemaker:
            wavemaker = "WK_LEFT_BC_IRR"
            pass
        elif 'LEF_SOL' in curwavemaker:
            wavemaker = "LEF_SOL"
            pass
        elif 'INI_SOL' in curwavemaker:
            wavemaker = "INI_SOL"
            pass
        elif 'INI_REC' in curwavemaker:
            wavemaker = "INI_REC"
            pass
        elif 'INI_GAU' in curwavemaker:
            wavemaker = "INI_GAU"
            pass
    wavemaker_list.bind('<<ListboxSelect>>', toggle_wavemaker_entries)

    # periodic boundary condition widgets
    pbc_cb = CheckB(pbc_frame, "Periodic Boundary Condition")
    pbc_cb.grid(row = 0)
    

    # warnings system
    # widget
    warnings_button = tk.Button(warnings_frame, text = "Validate")
    warnings_text = tk.Text(warnings_frame, height = 10, width = 40, wrap = tk.WORD)
    warnings_text.config(state = tk.DISABLED)
    warnings_scrollbar = ttk.Scrollbar(warnings_frame, orient = tk.VERTICAL,
                                        command = warnings_text.yview)
    warnings_text['yscrollcommand'] = warnings_scrollbar
    # main warnings logic function
    def validate():
        counter = 0
        # support function
        def insert(message):
            nonlocal counter
            warnings_text.insert(tk.END, "- " + message + "\n")
            counter += 1
        warnings_text.config(state = tk.NORMAL)
        warnings_text.delete('1.0', tk.END)
        ### Insert validation checks here 
        ## Model Validity Test
        if (mglob_led.get() == 0 or nglob_led.get() == 0
            or dx_lef.get() == 0 or dy_lef.get() == 0):
            insert("Global dimensions evaluate to 0")
        # wavemaker validation
        if isWavemaker.get():
            match wavemaker:
                case 'WK_REG':
                    # Bounds Checks
                    if (xc_wk_lef.get() > mglob_led.get() * dx_lef.get()):
                        insert("Out of Bounds x coordinate for wave maker")
                    if (yc_wk_lef.get() > nglob_led.get() * dy_lef.get()):
                        insert("Out of Bounds y coordinate for wave maker")
                    if (ywidth_wk_lef.get() > nglob_led.get() * dy_lef.get()):
                        insert("Invalid wave maker y width")
                    # Wave Validity
                    wavelength = 9.8 * tperiod_lef.get() * tperiod_lef.get() / 2 / 3.14
                    if (isFlat or isSlope) and wavelength > 2 * depth_flat_lef.get():
                        insert("Wave maker produces waves outside of resolution (lambda > 2h)")
                case 'WK_IRR':
                    pass
        ## File Checks
        if (isDepthData.get() and depth_data_les.get() == ""):
            insert("Depth data file not specified")
        if (friction_matrix_check.get() and friction_matrix_les.get() == ""):
            insert("Friction matrix file not specified")
        ### Cleanup and warnings counter
        warnings_text.insert("1.0", f"{counter :d} warnings\n")
        warnings_text.config(state = tk.DISABLED)
    warnings_button.configure(command = validate)
    # position
    warnings_button.grid(columnspan = 2)
    warnings_text.grid(row = 1)
    warnings_scrollbar.grid(row = 1, column = 2,
                            sticky = 'NSE')

    # input generation/params widgets and frame
    overwrite_cb = CheckB(igp_frame, text = "Overwrite?", value = True)
    gen_button = tk.Button(igp_frame, text = "Generate",
                           width = 25, height = 3,
                           command = generate)
    gen_button.grid(row = 1)
    overwrite_cb.grid(row = 0)

    overwrite_check_ttp = CreateToolTip(overwrite_cb.check, "Overwrites input.txt file when checked")
    m.mainloop()


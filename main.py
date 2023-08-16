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
    |   height_led.label.grid(row = 0, column = 0)# Place and position label in window
    |   height_led.entry.grid(row = 0, column = 1)# Don't forget the entry!
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
    |   height_lef.label.grid(row = 0, column = 0)# Place and position label in window
    |   height_lef.entry.grid(row = 0, column = 1)# Don't forget the entry!
    |   m.mainloop()
    '''
    def __init__(self, m, text) -> None:
        self.value = 0.0
        self.label = tk.Label(m, text = text)
        self.str = tk.StringVar(value = f"{self.value : f}")
        def set(var, index, mode):
            if (self.str.get().strip().replace(".", "", 1).isnumeric()):
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
    def generate():
        print("Generating input.txt")
        if overwrite.get():
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
        f.close()

    # Window Params
    m.geometry("1000x500")
    m.bind("<Configure>", center)

    # Frames
    parallel_frame = tk.Frame(m)
    dimension_frame = tk.Frame(m)
    time_frame = tk.Frame(m)
    depth_frame = tk.Frame(m)
    hotstart_frame = tk.Frame(m)
    physics_frame = tk.Frame(m)
    numerics_frame = tk.Frame(m)
    sponge_frame = tk.Frame(m)
    wavemaker_frame = tk.Frame(m)
    pbc_frame = tk.Frame(m)
    igp_frame = tk.Frame(m)
    parallel_frame.grid(row = 0, column = 0, sticky = "W")
    dimension_frame.grid(row = 1, column = 0, sticky = "W")
    time_frame.grid(row = 2, column = 0, sticky = "W")
    depth_frame.grid(row = 3, column = 0, sticky = "W")

    wavemaker_frame.grid(row = 0, column = 1, rowspan = 4, sticky = "N")
    pbc_frame.grid(row = 4, column = 1, sticky = "N")
    igp_frame.grid(row = 10, column = 3, sticky = "S")

    # Parallel Widgets
    parallel_label = tk.Label(parallel_frame, text = "Parallelization Arguments")
    px_led = LabelEntryD(parallel_frame, "PX")
    py_led = LabelEntryD(parallel_frame, "PY")
    px_led.set(os.cpu_count() / 2)
    py_led.set(1)
    # parallel pos
    parallel_label.grid(row = 0, columnspan = 2, sticky = "W")
    px_led.label.grid(row = 2, column = 0)
    px_led.entry.grid(row = 2, column = 1)
    py_led.label.grid(row = 3, column = 0)
    py_led.entry.grid(row = 3, column = 1)
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
    mglob_led.set(500)
    nglob_led.set(500)
    dx_lef.set(1.0)
    dy_lef.set(1.0)
    # dimension pos
    dimension_label.grid(row = 0, columnspan = 2, sticky = "W")
    mglob_led.label.grid(row = 1, column = 0)
    mglob_led.entry.grid(row = 1, column = 1)
    nglob_led.label.grid(row = 2, column = 0)
    nglob_led.entry.grid(row = 2, column = 1)
    dx_lef.label.grid(row = 3, column = 0)
    dx_lef.entry.grid(row = 3, column = 1)
    dy_lef.label.grid(row = 4, column = 0)
    dy_lef.entry.grid(row = 4, column = 1)

    # Time Widgets
    time_label = tk.Label(time_frame, text = "Time Arguments")
    time_total_lef = LabelEntryF(time_frame, "Total Time (s)")
    plot_int_lef = LabelEntryF(time_frame, "Output Interval (s)")
    screen_int_lef = LabelEntryF(time_frame, text = "Console Interval (s)")
    time_total_lef.set(300.0)
    plot_int_lef.set(1.0)
    screen_int_lef.set(1.0)
    # time pos
    time_label.grid(row = 0, columnspan = 2, sticky = "W")
    time_total_lef.label.grid(row = 1, column = 0)
    time_total_lef.entry.grid(row = 1, column = 1)
    plot_int_lef.label.grid(row = 2, column = 0)
    plot_int_lef.entry.grid(row = 2, column = 1)
    screen_int_lef.label.grid(row = 3, column = 0)
    screen_int_lef.entry.grid(row = 3, column = 1)

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
    depth_flat_lef = LabelEntryF(depth_frame, "Bottom Depth (m)")
    slope_lef = LabelEntryF(depth_frame, "Slope")
    xslope_lef = LabelEntryF(depth_frame, "Slope X Pos (m)")
    depth_data_label = tk.Label(depth_frame, text = "Filename")
    depth_data_entry = tk.Entry(depth_frame, textvariable= depth_data)
    depth_flat_lef.set(10.0)     
    slope_lef.set(0.05)
    xslope_lef.set(400)
    # depth pos
    depth_label.grid(row = 1, columnspan = 2, sticky = "W")
    flat_check.grid(row = 2, column = 0, sticky = "W")
    slope_check.grid(row = 3, column = 0, sticky = "W")
    depth_data_check.grid(row = 4, column = 0, sticky = "W")
    depth_flat_lef.label.grid(row = 2, column = 1)
    depth_flat_lef.entry.grid(row = 2, column = 2)
    # support funcs
    def show_flat_lef():
        depth_flat_lef.label.grid(row = 2, column = 1)
        depth_flat_lef.entry.grid(row = 2, column = 2)
    def show_slope_lef():
        depth_flat_lef.label.grid(row = 2, column = 1)
        depth_flat_lef.entry.grid(row = 2, column = 2)
        slope_lef.label.grid(row = 3, column = 1)
        slope_lef.entry.grid(row = 3, column = 2)
        xslope_lef.label.grid(row = 4, column = 1)
        xslope_lef.entry.grid(row = 4, column = 2)
    def show_data():
        depth_data_label.grid(row = 2, column = 1)
        depth_data_entry.grid(row = 2, column = 2)
    def hide_depth_entries():
        depth_flat_lef.label.grid_forget()
        depth_flat_lef.entry.grid_forget()
        slope_lef.label.grid_forget()
        slope_lef.entry.grid_forget()
        xslope_lef.label.grid_forget()
        xslope_lef.entry.grid_forget()
        depth_data_label.grid_forget()
        depth_data_entry.grid_forget()
        pass
    
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
    wavemaker_list.select_set(0)
    # wavemaker pos
    wavemaker_check.grid(row = 0, columnspan = 2, sticky = tk.N + tk.W)
    def show_wavemaker():
        wavemaker_list.grid(row = 1, column = 0)
        wavemaker_scrollbar.grid(row = 1, column = 1)
        toggle_wavemaker_entries("meme")
    def hide_wavemaker():
        wavemaker_list.grid_forget()
    def toggle_wavemaker_entries(event):
        pass
    wavemaker_list.bind('<<ListboxSelect>>', toggle_wavemaker_entries)

    # periodic boundary condition widgets

    # input generation/params widgets and frame
    overwrite = tk.BooleanVar(value = True)
    overwrite_check = tk.Checkbutton(igp_frame, text = "Overwrite?", variable = overwrite,
                                     onvalue = True, offvalue = False)
    gen_button = tk.Button(igp_frame, text = "Generate",
                           width = 25, height = 3,
                           command = generate)
    gen_button.pack(side = tk.BOTTOM)
    overwrite_check.pack(side = tk.BOTTOM)

    overwrite_check_ttp = CreateToolTip(overwrite_check, "Overwrites input.txt file when checked")
    m.mainloop()


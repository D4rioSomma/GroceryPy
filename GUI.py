import customtkinter as ctk
import pandas as pd
import os
from PIL import Image, ImageTk

GUIPyPath = os.path.dirname(os.path.abspath(__file__))

availableGUIThemes = ["blue", "green", "dark-blue"]
selectedGUITheme = availableGUIThemes[1]
availableGUIAppearanceMode = ["light", "dark"]
selectedGUIAppearanceMode = availableGUIAppearanceMode[0] # default, displayed in "light" mode

btnPad_x = 40
btnPad_y = 40

ctk.set_default_color_theme(selectedGUITheme)  # Themes: "blue" (standard), "green", "dark-blue"
ctk.set_appearance_mode("light")

def btnAppearanceEvent():
    global selectedGUIAppearanceMode

    if selectedGUIAppearanceMode == availableGUIAppearanceMode[0]:
        selectedGUIAppearanceMode = availableGUIAppearanceMode[1]
        ctk.set_appearance_mode(selectedGUIAppearanceMode)
    elif selectedGUIAppearanceMode == availableGUIAppearanceMode[1]:
        selectedGUIAppearanceMode = availableGUIAppearanceMode[0]
        ctk.set_appearance_mode(selectedGUIAppearanceMode)
    else:
        print("There is an error!\n")  

def addTodo():
    todo = entry.get()
    label = ctk.CTkLabel(addDataFrame, text=todo)
    label.pack()
    entry.delete(0, ctk.END)

### BEGIN Graphical settings ###
root = ctk.CTk()

iconPath = os.path.join(GUIPyPath, "Pics/GroceryPyIcon.ico")
iconImg = Image.open(iconPath)
iconLinuxImg = ImageTk.PhotoImage(iconImg)
root.tk.call('wm', 'iconphoto', root._w, iconLinuxImg)

GUIWidth  = 1200
GUIHeight  = 800

GUICornetOffset = 15 

# UP-LEFT CORNER
GUI_UL_x = (GUICornetOffset)
GUI_UL_y = (GUICornetOffset)
#exampleItem.place(x=GUI_UL_x, y=GUI_UL_y) 

# DOWN-LEFT CORNER
GUI_DL_x = (GUICornetOffset)
GUI_DL_y = (GUIHeight - 3*GUICornetOffset)
#exampleItem.place(x=GUI_DL_x, y=GUI_DL_y) 

# DOWN-RIGHT CORNER
GUI_DR_x = (GUIWidth - 10*GUICornetOffset)
GUI_DR_y = (GUIHeight - 3*GUICornetOffset)
#exampleItem.place(x=GUI_DR_x, y=GUI_DR_y) 

# UP-RIGHT CORNER
GUI_UR_x = (GUIWidth - 10*GUICornetOffset)
GUI_UR_y = (GUICornetOffset)
#exampleItem.place(x=GUI_UR_x, y=GUI_UR_y) 

root.geometry(f"{GUIWidth}x{GUIHeight}")
root.title("GroceryPy")
### END Graphical settings ###

### BEGIN Checkbox ###
btnAppearance = ctk.CTkButton(root, text="Appearance mode", command=btnAppearanceEvent, border_spacing = 5)
btnAppearance.pack(padx=btnPad_x, pady=btnPad_y)
btnAppearance.place(x=GUI_UR_x, y=GUI_UR_y) 

add_button = ctk.CTkButton(root, text="Add", width=250, command=addTodo)
add_button.pack(padx=btnPad_x, pady=btnPad_y)
### END Checkbox ###

### BEGIN Entry boxes ###

### END Entry boxes ###
title_label = ctk.CTkLabel(root, text="Daily Tasks", font=ctk.CTkFont(size=30, weight="bold"))
title_label.pack(padx=10, pady=(40, 20))

#scrollable_frame = ctk.CTkScrollableFrame(root, width=500, height=200)
#scrollable_frame.pack()

addDataFrame = ctk.CTkFrame(root, width=500, height=200)
addDataFrame.pack()
addDataFrame.place(x=GUI_DL_x, y=(GUI_DL_y - 100))

entry = ctk.CTkEntry(addDataFrame, placeholder_text="Item name")
entry.pack(fill="x")

### GUI visualization ###
root.mainloop()
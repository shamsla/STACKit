from tkinter import *
from tkinter import ttk, messagebox, filedialog
import os, shutil, bug,set_logo
from random import randrange
from icons import logoLabel
from files_extensions import *
from handle import *

#--------------------- Bug Window Functuions ---------------------
####################################################################
####################################################################
####################################################################
####################################################################
####################################################################
####################################################################
def bugTerminate():
    # After sending bug report
    # bug.bugbool -> True == sent | False == not sent
    if bug.bugbool:
        sukoon("Report Sent Successfully!", "#52de78")
        
    else:
        sukoon("Report Not Sent! Err. Occurred! (Internet ??)", "#eb5f52")

#---------------------- Main Window Functuions ---------------------
####################################################################
####################################################################
####################################################################
####################################################################
####################################################################
####################################################################
# All files extensions


def newer():
    # clears the pathInput field
    # and uncheck the new_folder checkbutton
    pathInput.delete(0, END)
    focusOut("pathInput", 1)
    if checkVar.get() == 1:
        newFolderRb.invoke()
    
def sukoon(message, color): # CHANGE THE MESSAGE LABEL
    # display the message with specific color 
    messLabel.config(text=message, background=color)
    lFrame.config(bg=color)




def separator(fileType, path):  # SEPARATES THE FILES
    # fileType - type of file as Images, Videos etc.

    

    i = 0  # INDICATES THAT FILES MOVED OR NOT (TRUE || FALSE)

    # getting all files in the given path
    filesList = os.listdir(path)

    if evaluate(fileType, path):
        # checking that if the files with the given fileType exists ot not
        # check evaluate for more 
        if not os.path.isdir(rf"{path}/{fileType}"):
            # creating folder for given fileType if it already not exists
            os.mkdir(rf"{path}/{fileType}")

    for f in filesList:
        if os.path.isfile(rf"{path}/{f}"):
            for ext in files[fileType]:
                if f.endswith(ext):
                    if os.path.exists(rf"{path}/{fileType}/{f}") == False:
                        # checking if there is any file with same  
                        shutil.move(rf"{path}/{f}", rf"{path}/{fileType}")
                        # increment in i to show that one or more files are moved
                        i += 1
                    else:
                        # if a file already exists with the same then change the name 
                        shutil.move(
                            rf"{path}/{f}", rf"{path}/{fileType}/Another_{randrange(991,100000)}_{f}")
                        i += 1
    if i > 0:
        # if one or more files are moved then return True otherwise retrurn False 
        # check above lines
        return True
    return False


def cSeparator(path, extension):  # CUSTOM FILES SEPARATOR

    # mainPath is simply the extension name in uppercase
    # removing . and spacing from extension(s)
    mainPath = ((extension.upper()).replace(".", "")).replace(" ", "")

    extension = (extension.replace(" ", "")).replace(".", "")

    if "," not in extension: # IF ONE EXTENSION IS GIVEN

        boolean = csMain(path, mainPath, extension)
        if boolean:
            if checkVar.get() == 1:
                otherFiles(path)
        return boolean

    else: # IF MORE EXTENSIONS ARE GIVEN
        if extension[-1] == "," or extension[0] == ",":
            return 3
        else:
            extension = extension.split(",")
            csDict = {} # STORES VALID AND INVALID EXTENSIONS, ( VALUE:BOOLEAN )

            tempExt = [] # EVALUATE DUPLICATE EXTENSIONS
            for ext in extension:
                if ext not in tempExt:
                    boolean = csMain(path, ((ext.upper()).replace(".", "")).replace(" ", ""), ext)
                    tempExt.append(ext)
                    csDict[ext] = boolean

            if any(csDict.values()):
                if checkVar.get() == 1:
                    otherFiles(path)

            falseStore = [] # STORE THE EXTENSIONS WHICH ARE NOT FOUND
            for key in csDict.keys():
                if csDict[key] == False:
                    falseStore.append(key)

            if len(falseStore) != 0:
                return falseStore
            else:
                return True

def arrange():  # MAIN FUNCTION FOR SEPARATING FILES ASSOCIATED WITH SEPARATE BTN
    

    path = pathInput.get()

    if path and path != "Enter Folder Path":
        if os.path.isdir(path):
            if os.listdir(path):
                if checkFiles(path):

                    # setting the label color back to normal
                    sukoon("", "#c2c2c2")

                    # getting the files type
                    entryText = mBEntry.get()
                    if entryText in ("Images", "Videos", "Audios", "Documents", "EXE Files", "Compressed"):
                        # if the fileType present in the above tuple
                        
                        # checks that if the files with the specific fileType exists or not
                        # check separator for more
                        otherIndicator = separator(entryText, path)
                        if otherIndicator:
                            # if true
                            if checkVar.get() == 1:
                                # if create new folder for other files option checked then move other files
                                otherFiles(path)

                            
                            sukoon("Files Successfully Separated!", "#52de78")
                            newer()

                        else:
                            # if false
                            sukoon(f"{entryText} Not Found!", "#eb5f52")

                    elif entryText == "Everything":

                        otherIndNum = 0
                        for i in files.keys():
                            otherIndicator = separator(i, path)
                            if otherIndicator:
                                otherIndNum += 1

                        if otherIndNum != 0:
                            if checkVar.get() == 1:
                                otherFiles(path)

                            sukoon("Files Successfully Separated!", "#52de78")
                            newer()

                        else:
                            
                            sukoon("Files Not Found!", "#eb5f52")

                    elif entryText:
                        if entryText != "Enter Files Extension":

                            boolean = cSeparator(path, entryText)

                            if boolean == False:

                                sukoon(
                                    "Files Not Found! (Check Your Extension)", "#eb5f52")

                            elif boolean == True:

                                sukoon("Files Successfully Separated!", "#52de78")
                                newer()
                                mBEntry.delete(0, END)
                                focusOut("mBEntry", 2)

                            elif boolean == 3:

                                sukoon("Invalid Extensions!", "#eb5f52")

                            elif type(boolean) == list:

                                mBEntry.delete(0, END)
                                mBEntry.insert(0, ','.join(boolean))

                                boolean = ','.join(boolean)
                                if len(boolean) > 29:
                                    boolean = f"{boolean[:30]} ..."

                                sukoon(
                                    f"Invalid Extensions : [ {boolean} ]", "#eb5f52")

                        else:

                            sukoon(
                                "Please Enter One | More Extensions!", "#eb5f52")
                else:

                    sukoon("Files Not Found! (Folder Without Files)", "#eb5f52")

            else:

                sukoon("Folder is empty!", "#eb5f52")

        else:

            sukoon("Invalid Path!", "#eb5f52")

    else:

        sukoon("Please Enter Folder Path!", "#eb5f52")

# ------------------------ GUI-FUNCTIONS----------------------------
####################################################################
####################################################################

def exitM():
    ask = messagebox.askyesno(title = "Exit", message = "Are You Sure?")
    if ask:
        root.destroy()

def infoAbout(i):
    if i == 1:
        ask = messagebox.askyesno(title="Information", message="STACKit\n\nYou can separate files like images and videos etc. easily using this application.\nYou just have to choose or enter the desired directory where your raw files are stored.\nThen select files type and click separate.\n\n** You can add multiple EXTENSIONS in CustomFiles OPTION.\n\t** Do You Want To Know How To Add Extensions ??")

        if ask:
            howExt()

    if i == 2:
        messagebox.showinfo(
            title="About", message="STACKit\n\nThis software is created for separating different type of FILES into different folders in just ONE CLICK.\n\nGitHub - https://github.com/shamsla")

def aboutExt():
    messagebox.showinfo(title="What Is File Extension",message="STACKit\n\nA filename extension is an identifier specified as a suffix to the name of a computer file.\nThe extension indicates a characteristic of the file contents or its intended use.\nA file extension is typically delimited from the filename with a full stop, but in some systems it is separated with spaces.\n\n** Check File Extension:\n\tRight Click On File > Click Properties >\n\tExtension will be at the end of the FILE NAME.")

def howExt():
    ask = messagebox.askyesno(title="How To - Extensions", message="Extensions\n\nIf you choose CustomFiles OPTION. You will have to enter FILE EXTENSION.\nFile Extension must be valid.\n\t(e.g. Image Files have Extensions like .jpg, .png etc.)\n\nYou can enter Extension with or without DOT like:\n\t( .jpg ) and ( jpg )\n\n** You can also add Multiple Extensions separated by COMA like:\n\tjpg , png , apk , exe\n\n** Do You Want To Know That What Are Extensions ??")

    if ask:
        aboutExt()

def focusIn(entry):
    if eval(entry).get() in ("Enter Folder Path", "Enter Files Extension"):
        eval(entry).delete(0, END)
    eval(entry).config(foreground="#000")

    sukoon("", "#c2c2c2")

def focusOut(entry, i):
    if not eval(entry).get():
        if i == 1:
            eval(entry).insert(0, "Enter Folder Path")
        else:
            eval(entry).insert(0, "Enter Files Extension")
        eval(entry).config(foreground="grey")

def rootBind():
    root.focus_set()

    sukoon("", "#c2c2c2")

def askD():
    ask = filedialog.askdirectory()
    if ask:
        pathInput.delete(0, END)
        pathInput.insert(0, ask)
        pathInput.config(foreground="#000")

def customType():
    mBEntry.delete(0, END)
    mBEntry.insert(0, "Enter Files Extension")

    mBtn.config(text="CUSTOM")
    mBEntry.pack(ipady=5, padx=(0, 4), anchor = "w")
    mBEntry.config(width=30)
    mBLabel.pack_forget()
    frame3.pack(pady=(14, 0))

def fileType(menuName):
    mBtn.config(text=menuName)
    mBEntry.pack_forget()
    mBLabel.pack(padx = (0, 20))
    frame3.pack(pady=(25, 0))

    mBEntry.delete(0, END)
    mBEntry.insert(0, menuName)

#------------------------ Main Window -----------------------------
####################################################################
####################################################################
####################################################################
####################################################################
####################################################################
####################################################################

root = Tk()
root.title("STACKit")
root.update_idletasks()
root.geometry(f"600x380+{(root.winfo_screenwidth()//2)-(600//2)}+{(root.winfo_screenheight()//2)-(380//2)}")
root.minsize(width=600, height=380)
root.maxsize(width=600, height=380)
root.update_idletasks()
root.geometry(f"600x380+{(root.winfo_screenwidth()//2)-(600//2)}+{(root.winfo_screenheight()//2)-(380//2)}")

# ---------------- ICON VALIDATE ------------------------
####################################################################
####################################################################

set_logo.setter(root)

#---------------------------------------------------

styler = ttk.Style()
styler.layout("TButton", [
    ("Button.focus", None),  # this removes the focus ring
    ("Button.background", {"children":
        [("Button.button", {"children":
            [("Button.padding", {"children":
                [("Button.label", {
                    "side": "left", "expand": 1})]
                })]
            })]
        })
])

# ----------------------- FRAMES -------------------------------
####################################################################
####################################################################
####################################################################
####################################################################


mainFrame = Frame(root)
mainFrame.pack(fill = "both")

# ----------------------- FRAMES OF mainFrame -------------------------------
####################################################################
####################################################################
####################################################################
####################################################################

bFrame = Frame(mainFrame)
bFrame.pack(pady = (30, 0))

lFrame = Frame(mainFrame, bg="#c2c2c2")
lFrame.pack(fill = X, pady = (44,0))

# ------------------------ SUB-FRAMES -------------------------
####################################################################
####################################################################

logo_frame = Frame(bFrame)
logo_frame.pack(fill = X)

frame1 = Frame(bFrame)
frame1.pack(pady = (30, 0), fill = X)

frame2 = Frame(bFrame)
frame2.pack(pady = (25,0), fill = X)

frame3 = Frame(bFrame)
frame3.pack(padx = (2,0), pady = (25,0), fill = X)

frame4 = Frame(bFrame)
frame4.pack(pady = (30,0), fill = X)

# ---------------------------- Menu ----------------------------
####################################################################
####################################################################
####################################################################
####################################################################

mainMenu = Menu(root)
root.config(menu=mainMenu)

fileMenu = Menu(mainMenu, tearoff = 0)
mainMenu.add_cascade(label = "File", menu = fileMenu)
fileMenu.add_command(label = "Select Folder", command = askD)
fileMenu.add_command(label = "Exit", command=exitM)

infoMenu = Menu(mainMenu, tearoff=0)
mainMenu.add_cascade(label="Info", menu=infoMenu)
infoMenu.add_command(label="STACKit", command=lambda: infoAbout(1))
infoMenu.add_command(label="How to Extensions", command = howExt)

helpMenu = Menu(mainMenu, tearoff=0)
mainMenu.add_cascade(label = "Help", menu=helpMenu)
helpMenu.add_command(label = "About Extensions", command=aboutExt)

helpMenu.add_command(label = "Report Bug", command = lambda:bug.bug(root, mainFrame, win_width = 600, win_height = 380, logo = logoLabel, terminator = bugTerminate, p_pad = 150, p_font_size = 10, p_speed = 15, p_length = 180))

aboutMenu = Menu(mainMenu)
mainMenu.add_command(label="About", command=lambda: infoAbout(2))

# ------------------ LOGO ----------------------
####################################################################
####################################################################

main_logo = logoLabel(120)
logo = ttk.Label(logo_frame,borderwidth=0,image=main_logo,cursor="hand2", compound="center", wraplength=0)
logo.pack(anchor = "center")

# -------------------- FRAME-1-WIDGETS -----------------------------
####################################################################
####################################################################
p_input_frame = Frame(frame1)
p_input_frame.grid(row = 0, column = 0)

p_entry_frame = Frame(frame1)
p_entry_frame.grid(row = 0, column = 1)

pathInput = ttk.Entry(p_input_frame, width=30, font=(
    "Courier New", "12"), foreground="grey")
pathInput.pack(ipady=5, padx = (0,2), ipadx = 1)
pathInput.insert(0, "Enter Folder Path")

pathBtn = ttk.Button(p_entry_frame, text="Browse", width = 12,cursor="hand2", command=askD)
pathBtn.pack(ipady=7, padx = (2,0))

# ----------------- FRAME-2-WIDGETS ------------------------------
####################################################################
####################################################################
mb_label_frame = Frame(frame2)
mb_label_frame.grid(row = 0, column = 0)

mb_entry_frame = Frame(frame2)
mb_entry_frame.grid(row = 0, column = 1)

mBLabel = ttk.Label(mb_label_frame, text="Select File Type : ")
mBLabel.pack(anchor = "w", padx = (0, 20))

mBEntry = ttk.Entry(mb_label_frame, font=("Courier New", "12"),foreground="grey")
mBEntry.insert(0, "Everything")

mBtn = ttk.Menubutton(mb_entry_frame, text="Everything", cursor="hand2")
mBtn.pack(anchor = "e")

mainMBtn = Menu(mBtn, tearoff=0)
mBtn["menu"] = mainMBtn
mainMBtn.add_command(label="Everything",
                     command=lambda: fileType("Everything"))

mainMBtn.add_command(
    label="Images", command=lambda: fileType("Images"))

mainMBtn.add_command(
    label="Videos", command=lambda: fileType("Videos"))

mainMBtn.add_command(
    label="Audios", command=lambda: fileType("Audios"))

mainMBtn.add_command(
    label="Documents", command=lambda: fileType("Documents"))

mainMBtn.add_command(
    label="EXE Files", command=lambda: fileType("EXE Files"))

mainMBtn.add_command(label="Compressed",
                     command=lambda: fileType("Compressed"))

mainMBtn.add_command(label="CUSTOM", command=customType)

# ------------------- FRAME-3-WIDGETS ---------------------------------
####################################################################
####################################################################

checkVar = IntVar()

newFolderRb = ttk.Checkbutton(frame3, text="Create New Folder For Other Files",
                              takefocus=0, cursor="hand2", variable=checkVar)
newFolderRb.pack(anchor = "w")

# -------------------------- FRAME-4-WIDGETS -----------------------
####################################################################
####################################################################

mainBtn = ttk.Button(frame4, text="SEPARATE", width=19,
                     cursor="hand2", command=arrange)
mainBtn.pack(ipady = 7, anchor = "center", fill = X)

# --------------- LAST-FRAME ---------------------------------
####################################################################
####################################################################

messLabel = ttk.Label(lFrame, text="", background="#c2c2c2", font=("Courier", 11, "bold"))
messLabel.pack(pady = 10)

# ----------------------------- BINDINGS ------------------------
####################################################################
####################################################################
####################################################################
####################################################################

mainFrame.bind("<Button>", lambda x: rootBind())
bFrame.bind("<Button>", lambda x: rootBind())
logo_frame.bind("<Button>", lambda x: rootBind())
frame1.bind("<Button>", lambda x: rootBind())
frame2.bind("<Button>", lambda x: rootBind())
frame3.bind("<Button>", lambda x: rootBind())
frame4.bind("<Button>", lambda x: rootBind())
lFrame.bind("<Button>", lambda x: rootBind())
mBLabel.bind("<Button>", lambda x: rootBind())
mBtn.bind("<Button>", lambda x: rootBind())
newFolderRb.bind("<Button>", lambda x: rootBind())
logo.bind("<Button>", lambda x: rootBind())

####################################################################
####################################################################

pathInput.bind("<FocusIn>", lambda x: focusIn("pathInput"))
pathInput.bind("<FocusOut>", lambda x: focusOut("pathInput", 1))
mBEntry.bind("<FocusIn>", lambda x: focusIn("mBEntry"))
mBEntry.bind("<FocusOut>", lambda x: focusOut("mBEntry", 2))

root.withdraw()
root.deiconify()

root.mainloop()
